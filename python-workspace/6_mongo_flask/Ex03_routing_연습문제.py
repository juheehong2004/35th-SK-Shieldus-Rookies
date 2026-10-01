from flask import Flask

app = Flask(__name__)

'''
문제 1 — /ping 경로로 접속하면 "pong"을 반환하는 라우트를 작성해 봅시다.
'''

@app.route("/ping")
def ping():
    return "pong"


'''
문제 2 — /servers/<server_name> 형태로 서버 이름을 받아 상태 메시지를 반환하는 동적 라우트를 작성해 봅시다.
'''

# http://localhost:5000/servers/웹서버 로 접속하면 (웹서버 가 파라미터와 같다고 보면됨)
# 웹서버 서버 상태 조회합니다. 라고 페이지 뜸
@app.route("/servers/<server_name>") #  <server_name> 은 파라미터와 같음
def servers(server_name):
    return f'{server_name} 서버 상태 조회합니다.'


# vs코드에서 재생 버튼 눌러서 웹 돌리기위함
if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1')