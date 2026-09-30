import schedule
import time
from datetime import datetime

# 1. 실행할 작업 정의 (함수화)
def daily_security_work():
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f"[{now}] 자동화 작업 시작...")

    # [연결] 실제로는 아래와 같이 기존 함수들을 순서대로 호출합니다
    # news = get_security_news()             # 8절: 뉴스 수집
    # create_excel_report(news)              # 10절: 엑셀저장
    # send_security_report(news)             # 9절: 메일발송

    print(f"[{now}] 작업 완료!")

# 2. 스케줄 등록
# schedule.every().day.at("16:39").do(daily_security_work) # 특정 시간
# schedule.every().wednesday.do(daily_security_work) # 특정 요일(해당 요일 정시에 실행됨)
# schedule.every().wednesday.at("16:42").do(daily_security_work) # 특정 요일(해당 요일 시간 설정)
schedule.every(10).seconds.do(daily_security_work) # 10초 마다



print("보안 자동화 비서가 가동되었습니다. 종료하려면 Ctrl+C를 누르세요.")

# 3. 무한 루프
while True:
    schedule.run_pending()   # 예약된 작업이 있는지 확인하고 실행
    time.sleep(1)             # 1초마다 체크 (CPU가 쉬게 해줍니다)