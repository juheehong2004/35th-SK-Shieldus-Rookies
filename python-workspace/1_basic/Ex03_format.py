


# -----------------------------------------
#  1.  문자열 포맷
name = "홍길동" 
age = 20 

 # f-string
print(f"이름: {name}, 나이: {age}")

# format() - 원래 순서 써야하는데 거의 생략함 -> 순서대로
print("이름: {}, 나이: {}".format(name, age)) # 이름: 홍길동, 나이: 20
print("이름2: {0}, 나이: {1}".format(name, age)) # 이름: 홍길동, 나이: 20
print("이름3: {1}, 나이: {0}".format(name, age)) # 이름: 20, 나이: 홍길동

 # % 연산자
print("이름: %s, 나이: %d" % (name, age))

print("이름:", name, ", 나이:", age) # format 형식 출력 아님
print()


# [1-1]. 문자열 포맷팅
user = "박길동"
target = "192.168.10.99"
action = "Login Success"
# [보안알림] 사용자 홍길동가 192.168.10.5 서버에 Login Failed 하였습니다.

# f-stirng
message = f"사용자 {user}가 {target} 서버에 {action} 하였습니다."
print(message)
# format()
print("사용자 {}가 {} 서버에 {} 하였습니다.".format(user, target, action))
# % 연산자
print("사용자 %s가 %s 서버에 %s 하였습니다."% (user, target, action))
print()




# [1-2]. 숫자 포맷팅
age = 25
score = 95
print(f"나이: {age}세")
print(f"점수: {score}점")

# 천 단위 쉼표 표시
money = 12345678
print(f'금액: {money:,}원')



# 자릿수지정 : 서버번호-00X
server_number = 3
print(f'서버번호-{server_number:3d}') # 서버번호-  3
print(f'서버번호-{server_number:03d}') # 서버번호-003



# [1-3]. 실수 포맷팅
cpu_usage = 33.1234
print(f'CPU 사용률 : {cpu_usage}%') # CPU 사용률 : 33.1234%
print(f'CPU 사용률 : {cpu_usage:.2f}%') # CPU 사용률 : 33.12%

mem_usage = 84.78912
#소수점1자리까지 출력
print(f'메모리 사용률 : {mem_usage:.1f}%') # 메모리 사용률 : 84.8% - 반올림됨 




#--------------------------------
# 2. 입력받기 - 입력 안됨 ㅜㅜ

# input으로 받으면 무조건 문자열임, 계산하려면 int 변환 필요
# name = input("이름을 입력하세요: ")
# age = int(input("나이를 입력하세요: "))
# print(f"이름: {name}, 나이: {age}")

'''
    [연습문제]
    서버이름(web)과 서버번호(1)를 입력받아 아래와 같이 출력되도록 하세요.

    [출력결과]
    서버: web-0001
'''
# server_name = input("서버이름을 입력하세요: ")
# server_number = int(input("서버번호를 입력하세요: "))
# print(f'서버: {server_name}-{server_number:04d}')


#--------------------------------
# 3. 임의의 수
import random

server_id = random.randint(1,45)
print(f'임의의 서버번호: {server_id:02d}') # 정수 랜덤값

server_id = random.uniform(1,45)
print(f'임의의 서버번호: {server_id:.2f}') # 실수 랜덤값

