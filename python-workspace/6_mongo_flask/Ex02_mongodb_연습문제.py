from pymongo import MongoClient
from datetime import datetime

client = MongoClient('mongodb://localhost:27017/') # 로컬 PC에서 실행 중인 MongoDB에 연결
db = client['security_db']  # security_db라는 데이터베이스를 선택
col = db['vulnerabilities'] # vulnerabilities라는 컬렉션을 선택(테이블)


'''
문제 1 — {"ip": "203.0.113.55", "action": "blocked"} 문서 한 건을 저장하는 코드를 작성해 봅시다.
'''
vuln_doc = {
    "ip": "203.0.113.55",
    "action": "blocked"
}

# document 삽입
result = col.insert_one(vuln_doc) # document 1개 추가
print(f'저장된 ID : {result.inserted_id}')



'''
문제 2 — severity가 Critical인 모든 문서를 조회해 title만 반복 출력하는 코드를 작성해 봅시다.
'''
# document 검색
data = col.find({"severity" : "Critical"})

for doc in data:
    print(doc["title"])