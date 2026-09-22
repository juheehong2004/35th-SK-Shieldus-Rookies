# [ 추가 연습문제  ]  딕셔너리 + 제어문

# 문제 1. 딕셔너리와 리스트를 조합해 보안 점검 정보 출력하기
# 딕셔너리와 리스트를 조합하면 여러 서버의 보안 점검 정보를 저장할 수 있습니다. 아래 실행 결과처럼 출력되도록 빈칸에 반복문과 `print()` 함수를 작성해 보세요.
'''
보안 점검 대상 서버
WEB-01 443번 포트
WEB-02 80번 포트
DB-01 3306번 포트
WAS-01 8080번 포트
'''

# 보안 점검 대상 서버 목록
servers = [
    {"name": "WEB-01", "port": 443},
    {"name": "WEB-02", "port": 80},
    {"name": "DB-01", "port": 3306},
    {"name": "WAS-01", "port": 8080}
]

print("보안 점검 대상 서버")

for server in servers:
    print(f'{server.get("name")} {server["port"]}번 포트')


print()

# 문제 2. 네트워크 로그에서 포트 번호별 접속 횟수 세기
# 네트워크 접속 로그에서 확인된 포트 번호
'''
결과
{80: 5, 443: 5, 22: 5, 3306: 3, 8080: 2}
'''
ports = [80, 443, 22, 80, 3306, 443, 22, 80, 8080, 443,
         22, 3306, 80, 443, 8080, 22, 80, 443, 3306, 22]

counter = {}

for port in ports:
    if(counter.get(port, "처음 접속") == "처음 접속"):
        counter[port] = 1
    else:
        counter[port] += 1

# 최종 출력
print(counter)


print()

# 문제 3 네트워크 장비 정보를 자료형에 따라 출력하기 `type()` 활용
# 네트워크 장비의 정보는 문자열, 숫자, 딕셔너리, 리스트 등 다양한 자료형으로 저장할 수 있습니다.
# `type()`을 활용해 자료형을 구분하고, **딕셔너리와 리스트 내부의 데이터까지 출력**해 보세요.
'''
결과
hostname : R1
ip : 192.168.10.1
http : 80
https : 443
protocol : TCP
protocol : UDP
protocol : ICMP
'''

# 네트워크 장비 정보를 저장합니다.
network = {
    "hostname": "R1",
    "ip": "192.168.10.1",
    "port": {
        "http": 80,
        "https": 443
    },
    "protocol": ["TCP", "UDP", "ICMP"]
}

# for 반복문을 사용합니다.
for key in network:
    network_value = network.get(key)
    # | 로 썼었는데 == 보다 우선순위가 낮아서 정상 작동 안했음
    if type(network_value) == list:
        for item in network_value:
            print(f'{key} : {item}')
    # type 확인할때 isinstance 함수 사용(비교1, 비교2) 
    elif isinstance(network_value, dict):
        for k, v in network_value.items(): # **** items() 써서 key, value 한번에 조회
            print(f'{k} : {v}')
    else:
        print(f'{key} : {network_value}')
    
    
    
