
'''
[ 연습문제-1] 실시간 네트워크 상태 점검

1. 접속 사용자 이름을 입력받는다.
2. IP 주소는 192.168.0.1 ~ 192.168.0.254 중 하나를 랜덤하게 생성한다.
    (예: 192.168.0.37)
3. 네트워크 지연시간(Ping)은 1.0 ~ 100.0ms 사이의 실수로 랜덤하게 생성한다.
    (소수점 1자리까지 표시한다.)
4.전송 데이터량은 1,000 ~ 1,000,000 사이의 정수로 랜덤하게 생성한다.
    (천 단위 콤마를 적용한다.)
5. 출력 예시: [네트워크 점검] 담당자: 홍길동 / IP: 192.168.0.37 / Ping: 23.4ms / 전송데이터량: 123,456byte
'''
import random

user_name = input("접속한 사용자의 이름을 입력하세요: ")
print(f'담당자: {user_name}')

ran_number = random.randint(1,254)
print(f'IP: 192.168.0.{ran_number}')

ran_number = random.uniform(1,100)
print(f'Ping: {ran_number:.1f}ms')

ran_number = random.randint(1000,100000)
print(f'전송데이터량: {ran_number:,}ms')
print()




'''
[ 연습문제-2 ] —  탐지 미니 리포트

1. 실행하면 "분석가 이름을 입력하세요:" 라고 묻는다.
2. 공격 출발 IP는 미리 준비된 문자열로 고정한다.
3. 실패 횟수는 5~50 사이에서 random으로 생성한다.
4. 위험도(risk_score)는 0~100 사이의 실수로 생성하고 소수점 1자리까지만 출력한다.
5. 출력 예시: `[브루트포스 탐지] 분석가: 이수진 / 203.0.113.55 실패 34회 / 위험도 82.6`

'''
import random

name = input('분석가 이름을 입력하세요: ')
start_ip = "203.0.113.55"
fail_count = random.randint(5,50)
risk_score = random.uniform(0,100)

print(f'[브루트포스 탐지] 분석가: {name} / 공격 출발 IP: {start_ip} / 실패 횟수: {fail_count}회 / 위험도: {risk_score:.1f}')


