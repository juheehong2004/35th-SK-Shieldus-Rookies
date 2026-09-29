# 2-1. 경로 
# os 방식: 문자열 더하기나 join 함수 사용
import os
os_path = os.path.join("security_logs", "2026", "weekly_report.txt")
print(f"OS 경로: {os_path}")

# pathlib 방식: / 기호로 직관적 연결
from pathlib import Path
pure_path = Path("security_logs") / "2026" / "weekly_report.txt"
print(f"Pathlib 경로: {pure_path}")

'''
절대경로 : 시작점부터 시작하는 경로 : 보통 / 으로 시작하는 경우
상대경로 : 기준점부터 시작하는 경로 : / 로 시작하지 않는 경우

. : 현재 디렉토리 의미
.. : 부모 디렉토리 의미
../.. : 부모의 부모 디렉토리
'''



# 2-2. 디렉터리 생성 및 존재 확인 — 감사 로그 저장소 준비
# os 방식
import os

# 해당 디렉토리에 폴더가 존재하지 않으면  
if not os.path.exists("security_logs1/daily"):
    os.makedirs("security_logs1/daily") # 폴더를 만들고
    # audit.log 파일이 있으면 열고 없으면 만들어 열어라(w-쓰기모드는 있으면 덮어씀)
    with open("security_logs1/daily/audit.log", "w") as f:
        f.write("audit start") # 해당 내용 작성해서 파일 열림
    file_name = os.path.basename("security_logs1/daily/audit.log")
    print(file_name)


# pathlib 방식
from pathlib import Path

# 'security_logs2/daily' 경로의 디렉터리(폴더)가 존재하지 않는 경우에만 아래 블록을 실행
if not Path("security_logs2/daily").exists():

    # 상위 디렉터리(security_logs2)까지 함께 생성하고(parents=True), 이미 폴더가 있어도 에러를 내지 않음(exist_ok=True)
    Path("security_logs2/daily").mkdir(parents=True, exist_ok=True)

    # 'security_logs2/daily/audit.log' 빈 파일을 생성함 (이미 존재할 경우 수정 시각만 업데이트)
    Path("security_logs2/daily/audit.log").touch()

    # 전체 경로에서 순수 파일 이름('audit.log')만 추출하여 file_name 변수에 저장
    file_name = Path("security_logs2/daily/audit.log").name

    # 추출한 파일 이름('audit.log')을 화면에 출력
    print(file_name)


# 2-3. 파일 목록 검색(Wildcard) — 오늘 생성된 로그만 찾기
# os 방식 (glob 모듈 따로 필요)

# 파이썬 표준 라이브러리인 glob 모듈을 가져옴 (파일 및 디렉터리 경로 패턴 매칭에 사용)
import glob

# 현재 디렉터리에서 확장자가 '.log'로 끝나는 모든 파일 경로를 리스트로 반환하여 변수에 저장함
log_files_os = glob.glob("*.log")
log_files_os = glob.glob("3_func/*.log")

# 탐색된 로그 파일 목록(리스트)을 화면에 출력함
print(log_files_os)


# pathlib 방식 (자체 지원)
# pathlib 모듈에서 파일 경로 처리를 담당하는 Path 클래스를 가져옴
from pathlib import Path

# 현재 디렉터리('.')에서 '.log'로 끝나는 모든 파일의 Path 객체를 구한 뒤 리스트 형태로 변환하여 저장함
log_files_path = list(Path(".").glob("*.log"))

# 찾은 로그 파일 목록(Path 객체들)을 하나씩 순회함
for file in log_files_path:
    # 각 파일의 이름(file.name)과 파일 크기(file.stat().st_size)를 바이트 단위로 출력함
    print(f"발견된 로그: {file.name}, 크기: {file.stat().st_size} bytes")




# 2-4. 파일 이동/복사/이름 변경 — 점검 완료 로그 아카이빙
# 객체 지향 경로 처리를 위한 pathlib과 파일 복사/이동 모듈인 shutil을 가져옴
from pathlib import Path
import shutil

# [1] 준비 작업
# 작업 대상 원본 파일 경로 객체 생성
source = Path("latest_scan.log")

# 원본 파일이 존재하지 않는 경우 테스트용 파일 생성 및 내용 작성 (UTF-8 인코딩)
if not source.exists():
    source.write_text("포트 스캔 : 3306 OPEN", encoding="utf-8")

# 아카이브 폴더 경로 객체 생성
archive_dir = Path("archive")

# 경로 연산자(/)를 사용하여 archive 디렉터리 내부의 복사본 파일 경로 생성
destination1 = archive_dir / "copy_scan.log"   # 경로 결합

# [2] 복사 및 이동 로직
if source.exists():
    # archive_dir.mkdir(exist_ok=True)

    # 복사 (원본 유지) — 감사팀 제출용 사본
    # shutil.copy(source, destination1)
    
    # 이동 (원본 삭제) — 처리 완료된 로그를 아카이브로 이동
    # shutil.move(source, Path('security_logs1/test.log'))
    # shutil.move(source, archive_dir)

    # 폴더 내 파일 목록 출력 (glob 사용)
    # file_list = list(archive_dir.glob("*.log"))
    # print(f'현재 log 파일 목록 : {file_list}')


    # 이름 변경 (rename) — 날짜별 스캔 이력 구분
    # new_path = archive_dir / "2026-09-28_scan.log"
    # destination1.rename(new_path)

    # 최종 전체 목록 확인
    # final_list = list(archive_dir.iterdir())
    final_list = list(Path('.').iterdir())
    print(f'최종 아카이브: {final_list}')