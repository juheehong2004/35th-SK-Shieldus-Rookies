## *** 순회 중 리스트 수정 금지, 변수 이름 의미 있게 짓기

## 3-1. range() — 포트 스캔 시뮬레이션
# 지정 범위만큼 반복문 실행
for n in range(10):
	print(n)

dan = int(input("구구단 단수를 입력하세요 -> "))
for n in range(10): # [0:10]
    print(f'{n} * {dan} = {n * dan}')

print()
# 21~25번 포트를 하나씩 점검
for port in range(21, 26):
    print(f"포트 {port} 점검 중...")

print()
# 100단위 포트를 점검
for port in range(1, 1000, 100):
    print(f"포트 {port} 점검 중...")

       
print()
## 3-2. 리스트 순회 — 스캔 대상 호스트 점검
scan_queue = ["prd-bastion-01", "prd-db-02", "prd-api-04"]

print("--- 전수 조사 시작 ---")
for host in scan_queue:
    print(f"[점검 중] 대상: {host} ... 연결 확인 완료")
print("--- 점검 종료 ---")

print()
## 3-3. 딕셔너리 순회 — CVE 카드 일괄 점검
cve_inventory = {
    "CVE-2026-30112": {"host": "prd-db-02", "cvss": 8.1, "patched": False},
    "CVE-2026-11450": {"host": "prd-api-04", "cvss": 9.4, "patched": True},
}

# items() 함수 미사용
for item in cve_inventory: 
    print(item) # key들만 출력됨

# items() 함수 사용
for item in cve_inventory.items(): 
    print(item) # key-value 같이 출력됨 - 단, 튜플로 출력됨

# items() 함수 사용, key-value 각각 출력
for key, value in cve_inventory.items():
    print(key, '-', value) # key들만 출력됨 - 튜플아니고 각각 출력됨


# cve_id = key / detail = value
for cve_id, detail in cve_inventory.items():
    status = "패치완료" if detail["patched"] else "미패치" # if 삼항연산자(한줄조건문), True면 왼쪽 문장 실행, False면 else 문장 실행
    print(f"{cve_id} | 호스트: {detail['host']} | CVSS: {detail['cvss']} | {status}")

print()
## 3-4. enumerate() — 로그 줄 번호와 함께 위험 패턴 탐지
auth_logs = ["Login success", "Failed password for root", "Logout", "Failed password for admin"]

for item in auth_logs:
    print(item) # 각 아이템 한줄씩 출력됨

# enumerate - 순회하면서 인덱스 필요할때 사용(인덱스 0부터 시작)
for item in enumerate(auth_logs):
    print(item) # (인덱스, 값) 튜플 형식으로 출력됨

for i, item in enumerate(auth_logs):
    print(i, item) # 인덱스, 값 형식으로 출력됨

# enumerate 인덱스를 0 대신 1로 시작
for line_num, log in enumerate(auth_logs, start=1): 
    if "Failed" in log: # log에 "Failed" 단어 있는지 없는지
        print(f"[경고] {line_num}번째 줄에서 보안 위협 감지: {log}")


print()
#============================================
'''
[ 문제 1 ]— 
    for문과 range()를 사용해서 1번부터 20번 포트 중 
    '짝수 번호'만 "포트 2 스캔 예정", "포트 4 스캔 예정" 형태로 출력해 봅시다. 
    (range()의 세 번째 인자, 간격을 활용하세요.)
'''
for i in range(1,20,2):
    print(f'포트 {i} 스캔 예정')

print()
'''
[ 문제 2 ]— 
    servers = ["WEB-01", "DB-01", "DB-02", "APP-01"] 리스트가 있습니다. 순회하면서 이름에 `"DB"`가 포함된 서버의 개수를 세어 `"DB 서버 총 2대"`처럼 출력해 봅시다.
'''
servers = ["WEB-01", "DB-01", "DB-02", "APP-01"]
count = 0

for server in servers:
    if(server.find('DB') == 0):
        count += 1

print(f'DB 서버 총 {count}대')

print()
'''
[ 문제 3 ]— 
    auth_logs = ["Login success", "Failed password", "Failed password", "Login success", "Failed password"] 리스트가 있습니다. 
    enumerate()를 사용해서 "Failed"가 포함된 로그의 **줄 번호와 내용**을 함께 출력하고, 
    반복이 끝난 뒤 총 실패 횟수도 출력해 봅시다.
'''
auth_logs = ["Login success", "Failed password", "Failed password", "Login success", "Failed password"]
fail_count = 0

for line, item in enumerate(auth_logs):
    if("Failed" in item):
        print(f'[실패] {line}번재 줄에서 로그인 실패 : {item}')
        fail_count += 1

print(f'총 실패 횟수 : {fail_count}')