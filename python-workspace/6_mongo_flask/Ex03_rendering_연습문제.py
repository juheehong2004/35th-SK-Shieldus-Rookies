'''
### 📝 연습문제 — 템플릿 렌더링

**문제 1** — `render_template('index.html', server_count=12)`처럼 정수 값을 넘기고 HTML에서 출력하는 코드를 작성해 봅시다.

**문제 2** — `blocked_ips` 리스트를 템플릿에서 `{% for %}`로 출력하는 코드를 작성해 봅시다.
'''

# app.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    alerts = [
        "[High] 방화벽 정책 위반 탐지 - 10.0.0.5",
        "[Medium] 반복 로그인 실패 - 203.0.113.55",
    ]
    return render_template('index3.html', alerts=alerts)

@app.route("/check")
def check():
    blocked_ips = ["172.15.22.124", "6.4.25.184.36", "128.128.128.2"]
    server_name = "Bastion-01"
    return render_template("index2.html"
                           , blocked_ips=blocked_ips
                           , server_name=server_name
                           )

if __name__ == "__main__":
    app.run(debug=True)