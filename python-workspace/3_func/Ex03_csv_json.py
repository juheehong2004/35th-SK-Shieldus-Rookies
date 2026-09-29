
# 3-1. with 블록 — 리소스를 안전하게 닫기

# 예전 방식 — 매번 f.close()를 신경써야 함
# f = open("security_log.txt", "w", encoding="utf-8")
# f.write("Admin login detected - 확인")
# f.close()

# with 블록 방식 — 실무에서는 이 방식을 사용
# with 블록을 벗어나는 순간, 에러 발생 여부와 상관없이 파일 리소스 종료를 빠르게 실행해줍니다
# with open("security_log.txt", "w", encoding="utf-8") as f:
#     f.write("Admin login detexted - 확인00")
    
    
# 에러가 나도, return을 해도, 그냥 블록만 끝나면 파일은 안전하게 닫힘!
# print("파일이 자동으로 닫혔습니다.")



## 3-2. CSV 파일 쓰기 — 일일 보안 점검 리포트

import csv

# 점검 데이터 (헤더 포함)
report_data = [
    ["호스트명", "IP_Address", "Status2", "Last_Check"],
    ["prd-web-01", "192.168.1.10", "Safe", "2026-08-29"],
    ["prd-db-02", "192.168.1.20", "Vulnerable", "2026-08-29"],
    ["prd-api-04", "192.168.1.30", "Safe", "2026-08-29"]
]

# csv 파일저장
# "w"는 write(덮어쓰기), "a"는 append(끝에 추가)
# 엑셀은 "utf-8-sig" 로 인코딩해야 한글 안깨짐
# with open("daily_security.csv", "w", newline='', encoding="utf-8-sig") as file:
#     writer = csv.writer(file) # csv에 file 연결
#     writer.writerows(report_data) # 반복문 대신


# print("CSV 보고서 생성이 완료되었습니다.")



## 3-3. 딕셔너리를 이용한 쓰기(DictWriter) — 침입 탐지 로그
import csv

# 딕셔너리 형태의 IDS/IPS 탐지 로그
logs = [
    {"target": "방화벽", "event": "포트 스캔", "severity": "High"},
    {"target": "IPS", "event": "SQL Injection", "severity": "Critical"},
    {"target": "WAF", "event": "XSS Attempt", "severity": "Medium"}
]

fieldnames = ["target", "event", "severity"]   # 엑셀의 맨 위 '열 이름' 정의

# with open("daily_log.csv", "w", newline='', encoding="utf-8-sig") as f:
#     writer = csv.DictWriter(f,fieldnames) # 딕셔너리 형태로 파일에 내용 작성
#     writer.writeheader() # 헤더 설정
#     writer.writerows(logs)









# [ 연습 ] daily_security.csv 파일을 읽어서 Status가 "Vulnerable"인 취약한 호스트를 찾아 호스트 이름과 IP 주소를 출력하는 코드를 아래에 작성하세요
# 원래 wt, rt 와 같이 text를 읽고쓴다고 써야하지만 생략 가능, 이미지 파일은 b
# 작성할때랑 똑같이 조건 작성해줘야함(w/r만 바뀜)
# with open("daily_security.csv", "r", newline='', encoding="utf-8-sig") as f:
#     reader = csv.DictReader(f)
#     # print(list(reader)) # 안됨
#     # 그냥 전체 읽기
#     # for row in reader:
#     #     print(row)

#     # 조건 읽기
#     for row in reader:
#         if row['Status2'] == 'Vulnerable':
#             print(f"취약 발견 : {row['호스트명']} : {row['IP_Address']}")







# 3-4. 파이썬 객체로 JSON 만들기 — json.dumps()
import json

# 보안 점검 결과 데이터 (파이썬 딕셔너리)
scan_result = {
    "target": "10.0.1.50",
    "status": "Critical",
    "open_ports": [22, 80, 443],
    "is_admin_exposed": True
}

# [1] 문자열로 변환 (indent는 가독성을 위한 들여쓰기)
# json_str = json.dumps(scan_result, indent=4) # dumps 의 s는 string
# print(json_str)

# [2] 파일로 직접 저장하기 — 슬랙 웹훅 전송이나 다음 배치 스크립트가 읽음
# with open("scan_report.json", "w", encoding="utf-8") as f:
#     json.dump(scan_result, f, indent=4) # dumps 가 아니고 dump


# 3-5. JSON을 파이썬 객체로 읽기 — json.loads()
with open("scan_report.json", "r", encoding="utf-8") as f:
    file_data = json.load(f)
    print(file_data['target'])