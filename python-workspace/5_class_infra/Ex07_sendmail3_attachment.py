'''
    기존에는 코드에 파일명을 지정하고 해당 파일을 첨부하였다.
    이번 예제에서는 첨부할 파일의 경로를 지정할 수 있다.
'''

import os
import smtplib
# [추가] 파일 첨부 데이터를 Base64로 인코딩합니다.
from email import encoders
# [추가] 일반 파일을 메일 첨부 형식으로 만듭니다.
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
# [추가] 첨부 파일 경로를 안전하게 처리합니다.
from pathlib import Path

from dotenv import load_dotenv

# .env 파일에 계정 정보를 분리 보관합니다.
load_dotenv()


# [추가] attachment_path 인자로 첨부할 파일 경로를 받습니다.
def send_security_report(news_list, to_email, attachment_path):
    user_email = os.getenv("NAVER_EMAIL_USER")
    app_password = os.getenv("NAVER_EMAIL_PASS")
    smtp_server = os.getenv("NAVER_SMTP_SERVER")
    smtp_port = int(os.getenv("NAVER_SMTP_PORT"))

    # [추가] 첨부 파일이 실제로 있는지 확인합니다.
    file_path = Path(attachment_path)
    if not file_path.is_file():
        print(f"첨부 파일을 찾을 수 없습니다: {file_path}")

    msg = MIMEMultipart()
    msg["Subject"] = "[자동 보고] 실시간 보안 뉴스 리포트"
    msg["From"] = user_email
    msg["To"] = to_email

    html_content = f"""
    <h3>[[ 알림 ]] 최신 보안 취약점 및 뉴스 목록</h3>
    <hr>
    <ul>
        {''.join(f'<li>{news}</li>' for news in news_list)}
    </ul>
    <p style="color:gray;">본 메일은 인프라 관리 시스템에 의해 자동 발송되었습니다.</p>
    """
    msg.attach(MIMEText(html_content, "html", "utf-8"))

    # [추가] 파일이 있을 때만 메일 첨부 형식으로 변환해 추가합니다.
    if file_path.is_file():
        with file_path.open("rb") as file:
            attachment = MIMEBase("application", "octet-stream")
            attachment.set_payload(file.read())

        encoders.encode_base64(attachment)
        attachment.add_header(
            "Content-Disposition",
            "attachment",
            filename=file_path.name,
        )
        msg.attach(attachment)

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(user_email, app_password)
            server.send_message(msg)
            print(f"[{user_email}] 메일 발송 성공!")
    except smtplib.SMTPException as error:
        print(f"메일 발송 중 오류 발생: {error}")


if __name__ == "__main__":
    to_email = input("받는 사람 이메일 주소를 입력하세요: ").strip()
    # [추가] 전송할 첨부 파일의 경로를 입력받습니다.
    attachment_path = input("첨부할 파일 경로를 입력하세요: ").strip()
    sample_news = ["Windows 커널 취약점 발견", "내부망 비정상 트래픽 탐지"]

    try:
        send_security_report(sample_news, to_email, attachment_path)
    except (FileNotFoundError, TypeError, ValueError) as error:
        print(f"오류 발생: {error}")