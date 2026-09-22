## 4-1. List Comprehension — 위험 CVSS만 추출

cvss_scores = [4.2, 9.8, 6.5, 7.1, 2.0, 9.1]

# 일반 반복문 버전
critical_scores = []
for score in cvss_scores:
    if score >= 7.0:
        critical_scores.append(score)

# 컴프리헨션 버전
# 반복문에서 나온 값을 바로 리스트에 추가
critial_score = [score for score in cvss_scores if score >= 7.0] 

print(f"1. 위험 등급(HIGH 이상) CVSS: {critical_scores}")





print()

## 4-2. Set Comprehension — 유니크 공격자 IP 추출

raw_attacker_logs = ["203.0.113.55", "203.0.113.99", "198.51.100.7", "203.0.113.55"]

# {} - Set 또는 Dict
# uniquq = {} 이렇게 만들면 기본은 딕셔너리로 됨

# 컴프리헨션 없이 set 만드는법 - set() 생성자 사용
set_data = set(raw_attacker_logs)
print(set_data) # {"203.0.113.55", "203.0.113.99", "198.51.100.7"} - 중복 제거됨

print(raw_attacker_logs[0]) # 203.0.113.55
print(raw_attacker_logs[0].split('.')) # ['203', '0', '113', '55']
print(raw_attacker_logs[0].split('.')[0]) # 203

# 컴프리헨션 사용 버전
unique_attackers = {ip for ip in raw_attacker_logs} # Set Comprehension 생성
print(f"고유 공격자 IP: {unique_attackers}") # {"203.0.113.55", "203.0.113.99", "198.51.100.7"}

# 조건 걸어서 Set 만들기
unique_attackers = {ip for ip in raw_attacker_logs if ip.split('.')[0] == '203'}
print(f"고유 공격자 IP: {unique_attackers}") # {"203.0.113.55", "203.0.113.99"}



print()

## 4-3. Dict Comprehension — 서버명 → IP 매핑 생성

servers = ["WEB", "DB", "PROXY"]

# 기본 딕셔너리 생성
server_map = {}
print(server_map) # {}

# 컴프리헨션 사용 딕셔너리 생성 (key : value 필요)
server_map = {server : f'서버: {server}' for server in servers}
print(server_map) # {'WEB': '서버: WEB', 'DB': '서버: DB', 'PROXY': '서버: PROXY'}

# 컴프리헨션 사용 딕셔너리 생성 - enumerate 활용 인덱스 가져오기
server_map = {server : f'10.0.0.{idx+1}' for idx, server in enumerate(servers)}
print(server_map) # {'WEB': '10.0.0.1', 'DB': '10.0.0.2', 'PROXY': '10.0.0.3'}




print()
#============================================
###  연습문제 
'''
[ 문제 1 ] — 
    ports = [22, 80, 443, 3306, 8080, 6379, 21] 리스트가 있습니다. 
    List Comprehension으로 1024 미만(잘 알려진 포트, well-known port)인 값만 뽑아 새 리스트를 만들어 봅시다.
'''
ports = [22, 80, 443, 3306, 8080, 6379, 21]

well_known_port = [port for port in ports if port < 1024]
print(well_known_port)


print()

'''
[문제 2] — 
    아래 CVE 리스트가 있습니다. 
    Set Comprehension을 사용해서 패치가 안 된(patched: False) CVE ID만 담은 Set을 만들어 봅시다.
'''
cve_list = [
    {"id": "CVE-2026-1001", "patched": False},
    {"id": "CVE-2026-1002", "patched": True},
    {"id": "CVE-2026-1003", "patched": False},
]
# 값은 동일하지만 순서가 주석과 다르게 나올 수 있습니다.

none_patched_id = {cve.get("id") for cve in cve_list if cve.get("patched") == False}
print(none_patched_id)


print()

'''
[문제 3 ] — 
    아래 코드가 생성하는 딕셔너리의 결과를 먼저 예측해보고, 실행해서 확인해 봅시다.
'''
hosts = ["bastion", "db", "cache"]
risk_map = {h: ("HIGH" if h == "db" else "LOW") for h in hosts}
print(risk_map) # {bastion : "LOW", "db" : "HIGH", "cache" : "LOW"}


