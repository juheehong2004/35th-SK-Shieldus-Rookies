# app.py
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# 실무에서는 이 리스트 대신 MongoDB에 저장합니다
security_events = ["방화벽 정책 위반 탐지 - 10.0.0.5", "반복 로그인 실패 - 203.0.113.55"]

@app.route('/')
def index():
    return render_template('index4.html', events=security_events)

# 입력받는곳도 보내는곳도 POST 여야함
# <form method="post" action="/events">
@app.route('/events', methods=['POST'])
def add_event():
    new_event = request.form.get('event')
    if new_event:
        security_events.append(new_event)
    return redirect(url_for('index')) # 등록 후 새로고침해서 페이지 보여줌
    # index라는 함수 이름이 / 경로에 매핑되어 있으니, url_for('index')를 호출하면 /라는 문자열을 반환
    # redirect(url_for('index'))는 결국 redirect('/')와 같은 동작을 하게 되는 거죠.

# 삭제 버튼 눌릴때
@app.route('/events/delete/<int:event_id>')
def delete_event(event_id):
    if 0 <= event_id < len(security_events):
        security_events.pop(event_id)
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)