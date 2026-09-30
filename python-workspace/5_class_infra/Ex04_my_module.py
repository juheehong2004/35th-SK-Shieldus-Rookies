
def add(a, b):
    return a + b

def hello(name):
    return f'{name}님 안녕하세요'

# 다른 파일에서 import 해서 실행할때 위에까지만 실행, main 내용은 실행 안됨
if "__name__" == "__main__":
    print(f'테스트 add : {add(2,3)}')
    print(f'테스트 add : {hello("박길동")}')