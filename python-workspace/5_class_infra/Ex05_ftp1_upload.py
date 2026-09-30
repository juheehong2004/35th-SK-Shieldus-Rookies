from ftplib import FTP
from pathlib import Path

def backup_log():
    HOST = "127.0.0.1" # 내 컴퓨터
    PORT = 2121

    # 로컬 파일 위치를 변수로 관리 
    BASE_DIR = Path(__file__).parent
    UPLOAD_FOLDER = BASE_DIR / "upload"
    # UPLOAD_FOLDER = "upload"
    SOURCE_FILE = "security_report.txt"

    # 서버에 저장할 파일명
    backup_file = "daily_report_backup.txt"

    # 폴더 + 파일명 결합
    local_file = Path(UPLOAD_FOLDER) / SOURCE_FILE

    # 1. 서버 접속 및 로그인
    with FTP() as ftp:
        ftp.connect(HOST, PORT)
        ftp.login("anonymous", "anonymous")

        print("--- FTP 서버 접속 완료 ---")

        ### 2. 파일 업로드
        with open(local_file, "rb") as f:
            ftp.storbinary(f'STOR {backup_file}', f)
        

        print("보안 리포트 백업(업로드) 성공!")


if __name__ == "__main__":
    backup_log()