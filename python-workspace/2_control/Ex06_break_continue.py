## 6-1. break — 치명적 발견 시 즉시 중단


servers_info = [
    {"name": "WEB-01", "usage": 40},
    {"name": "DB-01", "usage": 95},
    {"name": "APP-01", "usage": 30},
]

for server in servers_info:
    if server['usage'] >= 90:
        print(f"[긴급] 전체 점검 중단 : {server['name']} 서버가 사용량 초과 ({server['usage']}%)")



print()
## 6-2. continue — 화이트리스트 IP 건너뛰기

access_ips = ["1.1.1.1", "10.0.0.5", "2.2.2.2", "10.0.0.5"]
internal_whitelist = {"10.0.0.5", "100.0.0.22"}

for ip in access_ips:
    if ip in internal_whitelist:
        continue
    else:
        print(f'외부 {ip} 주소 위협 분석 중...')



print()

## 6-3. (심화) for-else — break 없이 끝났을 때만 실행
# for-else의 else는 반복문이 break로 중간에 끊기지 않고 끝까지 실행됐을 때만 동작
# "전체를 다 뒤졌는데도 못 찾았을 때"의 처리를 깔끔하게 표현할 수 있어 면접 단골 질문 중 하나

scanned_ports = [22, 80, 443, 8443]
dangerous_ports = {23, 3306, 6379}


for port in scanned_ports:
    if port in dangerous_ports:
        print(f'[위험 포트 발견] : {port}')
        break
else:
    print(f'위험 포트 없음 - 정상')


print()

#============================================
###  연습문제 — break / continue
'''
문제 1  — 
    ip_list = ["1.1.1.1", "2.2.2.2", "127.0.0.1", "3.3.3.3"]가 있습니다. 
    순회하다가 "127.0.0.1"을 만나면 "내부 루프백 발견 - 스캔 중단"을 출력하고 
    반복문을 즉시 빠져나오는 코드를 작성해 봅시다.
'''
ip_list = ["1.1.1.1", "2.2.2.2", "127.0.0.1", "3.3.3.3"]

for ip in ip_list:
    if(ip == '127.0.0.1'):
        print("내부 루프백 발견 - 스캔 중단")
        break
    print(ip)





print()
'''
문제 2  — 
    login_attempts = ["admin", "admin", "guest", "admin", "root"] 리스트가 있습니다. 
    "guest" 계정은 감사 대상에서 제외(continue)하고, 
    나머지 계정에 대해서만 "{계정} 로그인 시도 기록 분석 중"을 출력해 봅시다.
'''
login_attempts = ["admin", "admin", "guest", "admin", "root"]

for attempt in login_attempts:
    if(attempt == 'guest'): continue
    print(f'{attempt} 로그인 시도 기록 분석 중')

print()
'''
문제 3 — 
    open_ports = [22, 80, 443], blacklist_ports = {23, 3389, 6379}가 있습니다. 
    for-else를 사용해서, open_ports를 순회하며 blacklist_ports에 포함된 포트를 발견하면 
    즉시 "위험 포트 {포트} 발견 - 즉시 차단"을 출력하고 break하며, 
    끝까지 발견되지 않으면 "모든 포트가 안전합니다"를 출력해 봅시다.
'''
open_ports = [22, 80, 443]
blacklist_ports = {23, 3389, 6379}

for open in open_ports:
    for black in blacklist_ports:
        if(open == black): 
            print(f'위험 포트 {black} 발견 - 즉시 차단')
            break
else:
    print('모든 포트가 안전합니다')


