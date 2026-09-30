from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
from pathlib import Path

def run_ftp_server():
    authorizer = DummyAuthorizer()
    server_dir = Path(__file__).parent
    
    # 익명(anonymous) 접속 허용 및 읽기/쓰기 권한 부여
    authorizer.add_anonymous(server_dir, perm='elradfmw')

    handler = FTPHandler
    handler.authorizer = authorizer

    # 2121 포트에서 FTP 서버 대기 시작
    server = FTPServer(("0.0.0.0", 2121), handler)
    print("--- FTP 서버 실행 중 (포트: 2121) ---")
    server.serve_forever()

if __name__ == "__main__":
    run_ftp_server()