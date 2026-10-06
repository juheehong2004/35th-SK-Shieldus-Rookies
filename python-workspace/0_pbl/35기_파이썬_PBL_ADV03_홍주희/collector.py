'''
[파이썬 PBL 응용-3] KISA 보안공지 자동 수집 및 인프라 맞춤형 대시보드 구축
    - feedparser,pymongo 와 Flask 조건부 렌더링을 활용한 보안 위협 피드 수집 및 웹 모니터링 시스템 구현

[collector.py] 수집 담당 프로세스
    RSS 수집(feedparser) -> 중복 검사 후 MongoDB 저장(pymongo) -> 10분마다 자동 실행(schedule)
    실행 방법 : python collector.py   (종료는 Ctrl+C)
    ※ 웹 대시보드(app.py)와는 별도의 프로세스로 실행
'''
import time
from datetime import datetime
from pathlib import Path

import feedparser
import schedule
from pymongo import MongoClient

# ----------------------------------------------------------------------
# 설정값
# ----------------------------------------------------------------------
# KISA 보호나라 > 알림마당 > 보안공지 RSS (title / link / pubDate 3개 필드만 제공)
RSS_URL = "https://www.boho.or.kr/kr/rss.do?bbsId=B0000133"

# 사내 인프라에서 실제로 사용 중인 제품명 (제목에 하나라도 포함되면 감시 대상)
WATCH_VENDORS = ["Linux", "Cisco", "PostgreSQL"]

# 로그 파일 경로 (pathlib) : collector.py 가 있는 폴더 아래 logs/collector.log
BASE_DIR = Path(__file__).resolve().parent
LOG_DIR = BASE_DIR / "logs"
LOG_FILE = LOG_DIR / "collector.log"


def write_log(message):
    # 화면에 출력하고, 같은 내용을 로그 파일에도 남긴다 (자동 실행 중 상황 확인용)
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{now}] {message}"
    print(line)

    LOG_DIR.mkdir(parents=True, exist_ok=True)      # 폴더가 이미 있어도 에러 없음
    with LOG_FILE.open("a", encoding="utf-8") as f:  # a : 이어쓰기 모드
        f.write(line + "\n")


# ======================================================================
# 1. RSS 데이터 수집 및 파싱 (feedparser)
# ======================================================================
def fetch_advisories(rss_url=RSS_URL):
    """RSS 를 파싱해서 feed.entries 를 오래된 공지부터 순서대로 반환"""
    # RSS 주소에 접속해 XML 을 파싱
    # feed.entries 는 공지(entry) 하나하나가 담긴 리스트
    feed = feedparser.parse(rss_url)
 
    # 네트워크 오류 등으로 entry 를 하나도 못 받은 경우
    if feed.bozo and not feed.entries:
        write_log(f"RSS 수집 실패 : {feed.get('bozo_exception')}")
        return []
 
    # RSS 는 최신 공지가 맨 위에 있으므로 reversed() 로 오래된 것부터 처리
    # -> 나중에 저장되는(= collected_at 이 큰) 공지가 가장 최신 공지가 됨
    return list(reversed(feed.entries))


# ======================================================================
# 2. MongoDB 중복 검사 및 저장 (pymongo)
# ======================================================================
# MongoDB 연결 : 데이터베이스(security_db) -> 컬렉션(security_advisories)
# app.py 도 같은 컬렉션을 조회
client = MongoClient('mongodb://localhost:27017/', serverSelectionTimeoutMS=5000)
db = client['security_db']
col = db['security_advisories']


def save_advisories(entries):
    """link 가 같은 공지가 이미 있으면 건너뛰고, 신규 공지만 저장. 신규 저장 건수 반환"""
    new_count = 0

    for entry in entries:
        # 중복 체크 : 동일한 link 가 이미 컬렉션에 있으면 저장하지 않는다.
        exists = col.find_one({"link": entry.link})
        if exists:
            continue

        # 이 피드는 description/category 가 없으므로 title/link/published 만 꺼냄
        doc = {
            "title": entry.title,
            "link": entry.link,
            "published": entry.published,
            "collected_at": datetime.now(),
            # 감시 대상 판별 : 제목에 제품명이 하나라도 포함되면 True
            "is_watched": any(v in entry.title for v in WATCH_VENDORS),
        }
        col.insert_one(doc)
        new_count += 1

    return new_count

# ======================================================================
# 4. 자동화 스케줄링 및 운영 고려사항
# ======================================================================
def collect_advisories():
    """수집 -> 저장 한 번 실행하는 작업 (schedule 이 주기적으로 호출)"""
    try:
        entries = fetch_advisories()
        new_count = save_advisories(entries)
        write_log(f"공지 {len(entries)}건 확인, 신규 {new_count}건 저장 완료")
    except Exception as e:
        # MongoDB 연결 실패 등이 나도 프로그램이 죽지 않고, 다음 주기에 다시 시도
        write_log(f"수집 중 오류 발생 : {e}")


def run_scheduler():
    # 시작하자마자 1회 수집한 뒤, 이후 10분마다 반복 실행하도록 예약
    collect_advisories()

    # 10분마다 collect_advisories 실행을 예약 (함수 이름만 전달하므로 () 를 붙이지 않음)
    schedule.every(10).minutes.do(collect_advisories)

    write_log("KISA 보안공지 수집기가 가동되었습니다. 종료하려면 Ctrl+C를 누르세요.")

    # 예약된 작업이 있는지 계속 확인하는 무한 루프
    while True:
        schedule.run_pending()   # 실행할 시간이 된 작업이 있으면 실행
        time.sleep(1)            # 1초마다 확인 (CPU 과점유 방지)


# ======================================================================
# 메인
# ======================================================================
if __name__ == "__main__":
    try:
        run_scheduler()
    except KeyboardInterrupt:
        # Ctrl+C 로 종료할 때
        write_log("수집기를 종료합니다.")
