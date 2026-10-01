
#=================================
# 0. 연결 확인
# from pymongo import MongoClient

# try:
#     # MongoDB의 기본 포트 - 27017
#     client = MongoClient('mongodb://localhost:27017/', serverSelectionTimeoutMS=2000)
#     print(client.server_info().get('version'))
#     print("MongoDB 엔진 가동 확인 완료!")
# except Exception as e:
#     print("연결 실패: 서버가 꺼져 있거나 설치가 잘못됨.", e)

#====================================
# 1. CRUD 확인
from pymongo import MongoClient
from datetime import datetime

'''
서버종류(프로토콜):서버아이피주소:포트번호
http://127.8.9.7.80
mongodb://127.0.0.1:27017
'''


client = MongoClient('mongodb://localhost:27017/') # 로컬 PC에서 실행 중인 MongoDB에 연결
db = client['security_db']  # security_db라는 데이터베이스를 선택
col = db['vulnerabilities'] # vulnerabilities라는 컬렉션을 선택(테이블)

# [1] 입력하기 Insert
vuln_doc = {
    "cve_id": "CVE-2026-1234",
    "title": "OpenSSL 원격 코드 실행 취약점",
    "severity": "Critical",
    "affected_hosts": ["Bastion-01", "Bastion-02", "Bastion-03", "Bastion-04"],
    "collected_at": datetime.now()
}

# 저장
# result = col.insert_one(vuln_doc) # 데이터(레코드) 1개 추가(row)
# print(f'저장된 ID: {result.inserted_id}')

# [2] 검색하기  Select
data = col.find_one()
# data 딕셔너리에서 찾는 키값 없으면 "없음" 반환
print(f'찾는 데이터: {data.get("title", "없음")}')


# [3] 수정하기 Update - 검색 후 보면서 수정 해야함

# 검색 - "Severity" 키 : "Critical" 값 인 레코드(document)
data = col.find_one({"severity" : "Critical"})

# 수정 - status 컬럼 없으면 생성해서 추가함, 있으면 수정
# update_one : 조건 일치하는 도큐먼트 하나 만 수정
# update_many : 조건 일치하는 도큐먼트 전부 수정
col.update_one(
    {"cve_id" : data['cve_id']},
    {"$set" : {"Status": "No Patched"}}
)

# [4] 삭제하기 Delete

# 검색
data = col.find_one({"severity" : "Critical"})
# 삭제
col.delete_one({"cve_id" : data['cve_id']})
