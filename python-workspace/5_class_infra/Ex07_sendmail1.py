import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv

# 1. 환경변수 로드 (.env 파일에 계정정보를 분리 보관합니다)
load_dotenv()

def send_security_report(news_list, to_email):
    # .env 파일에서 정보 가져오기 (하드코딩 절대 금지)
    user_email = os.getenv("NAVER_EMAIL_USER")
    app_password = os.getenv("NAVER_EMAIL_PASS")
    smtp_server = os.getenv("NAVER_SMTP_SERVER")
    smtp_port = int(os.getenv("NAVER_SMTP_PORT"))  # 포트는 정수형으로 변환
    # user_email = os.getenv("GOOGLE_EMAIL_USER")
    # app_password = os.getenv("GOOGLE_EMAIL_PASS")
    # smtp_server = os.getenv("GOOGLE_SMTP_SERVER")
    # smtp_port = int(os.getenv("GOOGLE_SMTP_PORT"))  # 포트는 정수형으로 변환

    # 2. 메일 메시지 구성
    msg = MIMEMultipart()
    msg['Subject'] = "[자동 보고] 실시간 보안 뉴스 리포트"
    msg['From'] = user_email
    msg['To'] = to_email

    html_content = f"""
    <h3> [ 알림 ] 최신 보안 취약점 및 뉴스 목록</h3>
    <hr>
    <ul>
        {''.join([f'<li>{news}</li>' for news in news_list])}
    </ul>
    <p style="color:gray;">본 메일은 인프라 관리 시스템에 의해 자동 발송되었습니다.</p>
    """
    msg.attach(MIMEText(html_content, 'html'))

    # 3. 서버 접속 및 발송
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # 메일 서버와의 통신을 암호화합니다 (통신 구간 암호화)
            server.login(user_email, app_password)
            server.send_message(msg)
            print(f"[{user_email}] 메일 발송 성공!")
    except Exception as e:
        print(f"오류 발생: {e}")

if __name__ == "__main__":
    to_email = input("받는 사람 이메일 주소를 입력하세요: ")
    sample_news = ["Windows 커널 취약점 발견", "내부망 비정상 트래픽 탐지"]
    send_security_report(sample_news, to_email)