
# # 변수
# 변수 = '값'
# print(변수)

# # 자료형
# 정수 = 100
# 실수 = 2.8
# 문자열 = "안녕하세요"
# 문자열2 = '안녕하세요'
# print(정수)
# print(실수)
# print(문자열)

# n1ame = "홍길동"

# user-name = "홍길동"
# user@name = "홍길동"
# print(user-name)
# print(user@name)

"""
    프로그램 설명
"""

# import keyword          # keyword 모듈을 로딩
# print(keyword.kwlist)
# print(len(keyword.kwlist))

# -------------------------------
# 숫자형 처리에 에러나는 경우
a = 5
b = 2
add = a + b

print('a+b=', add)
# print('a+b=' + add) # 문자열 + 숫자 -> 에러


# -------------------------------
# 여러 변수 선언


# (*) 파이썬에서 두 변수의 값 바꾸기

print('a=', a, ', b=', b)

a, b = b, a
print('a=', a, ', b=', b) # 파이썬은 변수 값 바꿀때 temp 쓸 필요 없음

# \\192.168.45.123

print(10/3)
print(10//3)
print(10%3)

age = 25
print(age>=20 and age<30)


fruits = ["apple", "banana", "orange"]
print("Apple" in fruits) # 결과 : False