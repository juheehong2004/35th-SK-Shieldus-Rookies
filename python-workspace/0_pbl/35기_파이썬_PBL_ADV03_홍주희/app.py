'''
[파이썬 PBL 응용-3] KISA 보안공지 자동 수집 및 인프라 맞춤형 대시보드 구축
    - feedparser,pymongo 와 Flask 조건부 렌더링을 활용한 보안 위협 피드 수집 및 웹 모니터링 시스템 구현

[app.py] 웹 대시보드 담당 프로세스
    MongoDB 에 저장된 보안공지를 최신순 20건 조회 -> index.html 로 전달
    감시 대상 제품(is_watched=True) 공지는 템플릿에서 빨간색으로 강조
    실행 방법 : python app.py   ->   http://127.0.0.1:5000/
    ※ 수집기(collector.py)와는 별도의 프로세스로 실행
'''
from pathlib import Path

from flask import Flask, render_template
from pymongo import MongoClient
from pymongo.errors import PyMongoError

# ======================================================================
# 3. Flask 라우팅 및 템플릿 렌더링
# ======================================================================
# 템플릿 폴더 경로 (pathlib) : app.py 와 같은 위치의 templates/
BASE_DIR = Path(__file__).resolve().parent
app = Flask(__name__, template_folder=str(BASE_DIR / "templates"))

# collector.py 가 저장한 것과 같은 DB / 컬렉션을 조회
client = MongoClient('mongodb://localhost:27017/', serverSelectionTimeoutMS=3000)
db = client['security_db']
col = db['security_advisories']


@app.route('/') # "/" 주소로 접속하면 index() 를 실행
def index():
    advisories = [] # 조회한 공지 리스트
    error = None # 오류 메시지 (정상이면 None)

    try:
        # 최신순(collected_at 내림차순) 20건 조회 후 리스트로 변환
        # 같은 밀리초에 저장된 공지는 순서가 섞이므로 _id(저장 순서) 내림차순을 함께 사용
        advisories = list(
            col.find().sort([("collected_at", -1), ("_id", -1)]).limit(20)
        )
    except PyMongoError as e:
        # MongoDB 가 꺼져 있어도 웹 페이지가 500 에러로 죽지 않도록 안내 문구 표시
        error = f"MongoDB 조회 실패 : {e}"

    # 공지 리스트를 템플릿에 전달 (templates/index.html 에서 advisories, error 변수로 사용)
    return render_template('index.html', advisories=advisories, error=error)


# ======================================================================
# 메인
# ======================================================================
if __name__ == "__main__":
    # debug=True 는 운영 서버에서는 반드시 꺼야 하므로 False 로 둠
    app.run(host="127.0.0.1", port=5000, debug=False)
