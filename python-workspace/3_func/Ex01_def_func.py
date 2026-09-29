## 1-1. 함수 정의와 호출 — 서버 경보 발송

def send_alert(server_name, status):
    """서버 상태에 따른 경고 메시지를 생성하는 함수""" 
    # Docstring은 ai와 팀원을 위해 꼭 작성하는것을 권장함
    print(f"🔴 [경보] 대상 장비: {server_name}")
    print(f"🔴 [상태] 현재 상황: {status}")
    print("-" * 20)


# 함수 호출 (이름만 부르면 실행됨)
send_alert('prd-db-02', 'CPU과부화')
print('-' * 40)
send_alert('prd-web-03', '비정상 로그인 감지')






## 1-2. Docstring — 동료가 코드를 열지 않고도 이해하게 만들기

# 함수 위에 마우스를 올리면 Docstring 내용이 툴팁으로 뜬다.
def check_port_status(port_number):
    """
    특정 포트 번호가 보안 정책상 허용된 포트인지 확인하는 함수.

    Args:
        port_number (int): 점검할 포트 번호
    Returns:
        bool: 허용 여부 (True: 안전, False: 위험)
    """
    allowed_ports = [80, 443, 22]
    return port_number in allowed_ports



# 함수 호출
result = check_port_status(80)
print(f'허용된 포트번호 : {result}') # 허용된 포트번호 : True

# 짧게 줄이기
print(f'허용된 포트번호 : {check_port_status(8800)}') # 허용된 포트번호 : False

# bool(True, False)의 값으로 True면 '안전' 출력, 그렇지 않으면 '위험' 출력
print(f"허용된 포트번호 : {'안전' if check_port_status(80) else '위험'}")



## 1-3. 스코프(Scope) — 전역 상태를 함수가 실수로 건드리지 않도록
firewall_policy = "차단"

def change_policy():
    firewall_policy = "허용"
    print(f"함수 안 정책: {firewall_policy}") # 허용

change_policy()
print(f"최종 정책: {firewall_policy}") # 차단







## 1-4. 전역변수를 수정 — 허용 IP 목록 수정
"""
# 전역 변수 allowed_ips
allowed_ips = ["10.0.0.1", "20.1.1.2"]

# 전역 변수 allowed_ips에 추가하는 함수를 여기에 작성합니다.
def add_ip(new_ip):
    '''
    매개변수로 넘어오는 새로운 아이피 주소를 전역 변수 allowed_ips에 추가하는 함수

    Args:
        new_ip(str) : 추가할 새로운 아이피 주소
    Returns:
        None
    '''
    allowed_ips.append(new_ip)

# add_ip 함수 호출
add_ip("10.0.0.2")

print(f"함수 외부 리스트: {allowed_ips}")   # ['10.0.0.1', '20.1.1.2', '10.0.0.2'] — 같이 바뀜
"""

# 함수 외부에서 허용 IP 목록을 출력하려면??? - return으로 반환해서 출력함
def add_ip(new_ip):
    # 지역 변수(함수 내 변수)
    allowed_ips = ["10.0.0.1", "20.1.1.2"]

    allowed_ips.append(new_ip)
    print(f"함수 내부 리스트: {allowed_ips}")
    return allowed_ips

# add_ip 함수 호출
print(f"함수 외부 리스트: {add_ip('10.0.0.2')}")






# 1-5. 유연하게 매개변수와 반환 
def filter_high_risk(server_list):
    """위험 수치가 높은 서버 이름만 리스트로 반환"""
    return [s for s in server_list if s['risk'] > 80]

inventory = [
    {"name": "prd-web-01", "risk": 95},
    {"name": "prd-db-02", "risk": 40},
    {"name": "prd-bastion-01", "risk": 70},
    {"name": "prd-db-04", "risk": 80},
]
result = filter_high_risk(inventory)
print(result )  # [{'name': 'prd-web-01', 'risk': 95} ]


# 1-6. 매개변수 기본값 — 점검 포트 기본값 지정
def scan_network(ip_addr="127.0.0.1", port_number=80):
    """지정된 IP와 포트를 스캔한다. 포트를 안 적으면 80번을 기본으로 한다."""
    print(f"{ip_addr} : {port_number} 접속하였습니다.")

scan_network("192.168.0.1", 443)   # 포트: 443
scan_network("192.168.0.1")        # 포트: 80

scan_network() # 아이피주소 : 127.0.0.1, 포트:80

# 1-7. 가변 인자 *args — 여러 대의 서버를 한 번에 점검 - args는 튜플
# args는 익숙해지면 *servers와 같이 이름 변경해도됨
def check_servers(*args):
    """입력된 모든 서버를 순회하며 점검"""
    print(f'총 {len(args)}대의 서버 점검 시작...')
    for arg in args:
        print(f'-> {arg} 점검중')

# 몇 개를 넣어도 상관없음
check_servers("prd-web-01") # ('prd-web-01', ) -> 요소 한개일때 (요소1 ,) 이어야 튜플
check_servers("prd-db-02", "prd-api-04", "stg-cache-01") # ('prd-db-02', 'prd-api-04', 'stg-cache-01')
check_servers("prd-db-02", "prd-api-04", "stg-cache-01","stg-cache-05") # ('prd-db-02', 'prd-api-04', 'stg-cache-01', 'stg-cache-05')




# 1-8. 가변 인자 **kwargs = keyword 인자(args) - **kwargs는 딕셔너리

# def update_config(server_name, os, port, status, backup, zone):
def update_config(server_name, **kwargs):
    # **kwargs는 익숙해지면 **options 같이 수정해도됨
    """서버의 설정을 가변적으로 업데이트"""
    print(f"[{server_name}] 설정 변경 내역")
    for key, value in kwargs.items():
        print(f"{key} : {value}")

# 옵션 이름을 내 마음대로 정해서 던질 수 있음
update_config("prd-web-01", os="Linux", port=80, status="Active")
update_config("prd-db-02", backup="Daily", zone="Asia-Northeast")






# 1-9. 실수 사례 — 가변 인자 순서 문제

# 실수 1: *args 뒤에는 반드시 이름이 있는 키워드 인자만 올 수 있다
def scan_server(*targets, port):
    for t in targets:
        print(f"{t}:{port} 점검 중")

# 호출 시 port는 반드시 키워드로 지정해야 함
# scan_server("1.1.1.1", "2.2.2.2", 80) # TypeError: 
scan_server("1.1.1.1", "2.2.2.2", port=80)

# 실수 2: *args를 두 개 이상 선언할 수는 없다
# def check_assets(*ips, *hostnames): -> SyntaxError

# 실수 3: **kwargs 뒤에는 *args가 논리적으로 올 수 없다
# def update_config(**options, *args): -> SyntaxError
# 이유: **kwargs는 '이름표가 붙은 모든 것'을 다 가져가버리기 때문에
# 그 뒤에 이름표 없는 *args가 오는 건 문법적으로 성립하지 않는다




# 1-10. 람다(Lambda) — 점검용 일회용 함수

# 일반 함수
def is_privileged_port(port):
    return port < 1024

print(is_privileged_port(22))   # True

# 람다 함수 (위와 동일)
# lambda 매개변수 : 반환값
is_privileged_port = lambda port: port < 1024
print(is_privileged_port(22)) # True


# 1-10-1 filter() - 필터링
# 보안 로그에서 특정 위험 수치 이상만 뽑아낼 때 유용하다.
risk_scores = [10, 45, 88, 20, 95, 70]

# 80점 이상(고위험)만 필터링 - filter 객체로 반환됨
danger_hosts = filter(lambda x: x > 80, risk_scores)
print(danger_hosts) # <filter object at 0x000001F7F828BB20>

# filter 객체를 내가 출력할 형태로 변환
danger_hosts = list(filter(lambda x: x > 80, risk_scores))
print(danger_hosts) # [88, 95]


# 1-10-2 map() - 일괄 적용
# 전체 IP 리스트 앞에 특정 태그를 붙이거나 형식을 바꿀 때 쓴다.
blocked_ips = ["1.1.1.1", "2.2.2.2", "3.3.3.3"]

# 모든 IP 앞에 [BLOCKED] 태그 붙이기
blocked_tag = map(lambda ip: f'[BLOCKED] {ip}', blocked_ips)
print(blocked_tag) # <map object at 0x0000024D1F38BB80>
print(list(blocked_tag)) # ['[BLOCKED] 1.1.1.1', '[BLOCKED] 2.2.2.2', '[BLOCKED] 3.3.3.3']

# lamda 를 일반 함수로 작성한다면?
def test():
    return f'[BLOCKED] {ip}'



# 1-10-2 sorted() — 정렬
# 딕셔너리 리스트를 특정 키값(예: 위험 점수) 순으로 정렬할 때 필수다.
servers = [
    {"name": "prd-web-01", "risk": 40},
    {"name": "prd-db-02", "risk": 90},
    {"name": "prd-api-04", "risk": 75}
]

# risk 점수를 기준으로 오름차순 정렬 (기본 reverse=False)
# sorted 함수가 servers를 순환하면서 순서대로 lambda 함수에 전달해줌 = s
sorted_servers = sorted(servers, key=lambda s: s['risk'])
print(sorted_servers)

# risk 점수를 기준으로 내림차순 정렬
sorted_servers = sorted(servers, key=lambda s: s['risk'], reverse=True)
print(sorted_servers)


# [ 연습문제 ]