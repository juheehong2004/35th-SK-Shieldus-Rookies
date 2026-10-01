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



if __name__ == "__main__":
    app.run(debug=True)