'''
### 📝 연습문제 — 클래스 · 생성자 · self

**문제 1**  — `FirewallRule` 클래스를 만들고, `__init__(self, rule_id, ip, action)`으로 규칙 번호·IP·허용/차단(action)을 저장한 뒤, 인스턴스를 하나 생성해서 각 속성을 출력하는 코드를 작성해 봅시다.

```jsx

# 출력확인
rule1 = FirewallRule(1001, "203.0.113.55", "DENY")
print(f"규칙 {rule1.rule_id}: {rule1.ip} -> {rule1.action}")
```
'''

class FirewallRule:
    def __init__(self, rule_id, ip, action):
        self.rule_id = rule_id
        self.ip = ip
        self.action = action

rule1 = FirewallRule(1001, "203.0.113.55", "DENY")
print(f"규칙 {rule1.rule_id}: {rule1.ip} -> {rule1.action}")


'''
**문제 2** — 위 `Server` 클래스에 `restart(self)` 메서드를 추가해서, 호출 시 `self.status`를 `"Restarting"`으로 바꾸고 `"{name} 서버를 재시작합니다"`를 출력하도록 만들어 봅시다.

```jsx

# 출력확인
web_svr = Server("WEB-01", "192.168.1.10")
web_svr.restart()   # WEB-01 서버를 재시작합니다
print(web_svr.status)  # Restarting
```
'''
class Server:
    def __init__(self, name, ip):
        self.name = name
        self.ip = ip

    def restart(self):
        self.status = "Restarting"
        print(f"{self.name} 서버를 재시작합니다")

web_svr = Server("WEB-01", "192.168.1.10")
web_svr.restart()   # WEB-01 서버를 재시작합니다
print(web_svr.status)  # Restarting


'''
**문제 3**  — `self`는 왜 인스턴스 메서드의 첫 번째 매개변수로 반드시 필요한지, 그리고 `self`를 빼고 메서드를 정의하면 실제로 어떤 에러가 나는지 설명해 봅시다.

- 객체마다 서로 다른 데이터를 구별하기 위해 사용합니다. 여러 인스턴스가 있어도 self만 사용하면 헷갈리지 않습니다.
- 에러가 나는 이유
greet() 함수는 매개변수를 0개 받도록 정의되어 있습니다.
하지만 인스턴스를 통해 p.greet()를 호출하면, 파이썬은 자동으로 인스턴스 p라는 1개의 인자를 전달합니다.
전달된 인자(1개)와 정의된 매개변수(0개)의 개수가 맞지 않아 TypeError가 나타납니다.

- 인스턴스 메서드를 호출하면 파이썬이 해당 인스턴스 객체를 자동으로 첫 번째 인자로 전달하므로, 이를 받아주기 위해 self 매개변수가 필수적입니다. 생략 시 인자 개수 불일치로 인한 TypeError가 발생합니다.
'''







'''
### 📝 연습문제 — 추상화 · 캡슐화

**문제 1** — `LogEntry` 클래스를 만들고, `__init__(self, ip, level, message)`로 로그 한 줄의 핵심 정보(IP, 로그 레벨, 메시지)만 추상화해서 저장하는 코드를 작성해 봅시다.

```jsx

# 출력
log1 = LogEntry("203.0.113.55", "ERROR", "Failed to connect to DB")
print(f"[{log1.level}] {log1.ip} - {log1.message}")
```
'''
class LogEntry:
    def __init__(self, ip, level, message):
        self.ip = ip
        self.level = level
        self.message = message

log1 = LogEntry("203.0.113.55", "ERROR", "Failed to connect to DB")
print(f"[{log1.level}] {log1.ip} - {log1.message}")


'''
**문제 2** — 위 `SecuritySystem` 클래스에 `change_password(self, old_pw, new_pw)` 메서드를 추가해서, `old_pw`가 맞을 때만 `self.__admin_pw`를 `new_pw`로 바꾸도록 만들어 봅시다.

```jsx

# 출력

security = SecuritySystem()
security.change_password("wrong", "new_secret")   # 실패
security.change_password("secret123", "new_secret")  # 성공
```
'''
class SecuritySystem:
    def __init__(self):
        self.__admin_pw = "secret123"  # __를 붙여 외부 접근 차단 (캡슐화)
        self.admin_name = "admin"

    def login(self, input_pw):
        if input_pw == self.__admin_pw:
            print("로그인 성공")
        else:
            print("접근 거부")

    def __internal_check(self):
        # 이름 앞에 __가 붙으면 클래스 내부에서만 호출 가능합니다
        print("내부 점검 중")

    def change_password(self, old_pw, new_pw):
        if self.__admin_pw == old_pw:
            self.__admin_pw = new_pw
            print("비밀번호 변경 성공")
        else:
            print("비밀번호 변경 실패")

security = SecuritySystem()
security.change_password("wrong", "new_secret")   # 실패
security.change_password("secret123", "new_secret")  # 성공


'''
**문제 3** — 관리자 비밀번호, API 키 같은 민감한 값을 클래스 안에서 다룰 때 왜 `__`를 붙여 캡슐화하는 습관이 필요한지, 그리고 이것이 완벽한 보안 대책은 아닌 이유를 함께 설명해 봅시다.

- 실수로 값이 수정되지 않도록 방지하기 위해.
하지만 완벽 차단은 아니고 우회해서 접근할수있으므로 완벽한 보안 대책은 아님

- 파이썬의 __ 캡슐화는 완벽한 접근 차단이 아니라 네임 맹글링(name mangling)이라는 기법입니다. 실제로는 _SecuritySystem__admin_pw라는 이름으로 변경되어 저장될 뿐이라, 마음만 먹으면 우회 접근이 가능합니다. 그래서 실무에서는 이를 "강제 차단"이 아니라 "실수로 잘못 건드리지 않도록 하는 관례적 신호"로 이해해야 합니다.
'''







'''
### 📝 연습문제 — 상속 · 다형성

**문제 1**  — 위 예제에 있는 `BaseServer`를 상속받는 `DBServer` 클래스를 만들고, `check()`를 오버라이드해서 `"{name} DB 서버 점검..."`을 출력하도록 작성해 봅시다.
'''
from abc import ABC, abstractmethod

class BaseServer(ABC):
    def __init__(self, name: str, ip: str):
        self.name = name
        self.ip = ip
        self.status = "Unknown"

    @abstractmethod
    def check(self):
        pass  # 자식 클래스가 반드시 재정의해야 하는 추상 메서드

    def power_on(self):
        print(f"{self.name} 서버 전원 켜기")
        self.status = "Running"

class DBServer(BaseServer):
    def check(self):
        print(f'{self.name} DB 서버 점검...')

dbServer = DBServer("naver", 192)
dbServer.check()

'''
**문제 2**  — `WebServer`와 `DBServer` 인스턴스를 하나씩 만들어 리스트에 담고, `for`문으로 순회하며 `power_on()`과 `check()`를 각각 호출해 결과가 서버 타입마다 다르게 나오는 것을 확인해 봅시다.
'''
from abc import ABC, abstractmethod

class BaseServer(ABC):
    def __init__(self, name: str, ip: str):
        self.name = name
        self.ip = ip
        self.status = "Unknown"

    @abstractmethod
    def check(self):
        pass  # 자식 클래스가 반드시 재정의해야 하는 추상 메서드

    def power_on(self):
        print(f"{self.name} 서버 전원 켜기")
        self.status = "Running"


class WebServer(BaseServer):
    # 추상 메서드 구현
    def check(self):
        print(f"{self.name} 웹 서버 점검...")

    def run_service(self):
        print("웹 서비스(80/443) 가동!")


class DBServer(BaseServer):
    def check(self):
        print(f"{self.name} DB 서버 점검...")

    def run_service(self):
        print("DB 서비스(3306) 가동!")

webServer = WebServer("WebServer", "192")
dbServer = DBServer("DBServer", "200")

server_list = [webServer, dbServer]

for server in server_list:
    server.check()
    server.power_on()


'''
**문제 3**  — 상속과 다형성을 활용해 서버 종류별 클래스를 나눠 설계했을 때, `APIServer`라는 새로운 서버 타입이 추가되는 상황에서 기존 코드(예: 전체 서버 점검 루프)를 얼마나 수정해야 하는지 설명해 봅시다.

기존 코드는 수정할 필요 없음.
APIServer 내부에 부모 클래스의 추상 메소드를 오버라이딩하여 구현하면됨.
'''






'''
### 📝 연습문제 — 모듈 · 패키지

**문제 1** — `ipaddress` 모듈로 `"10.0.0.0/8"` 대역에 `"10.5.5.5"`가 포함되는지 확인하는 코드를 작성해 봅시다.
'''
import ipaddress

# 10.0.0.0/8 대역을 네트워크 객체로 생성합니다
network = ipaddress.ip_network("10.0.0.0/8")
target_ip = ipaddress.ip_address("10.5.5.5")

# in 연산자로 특정 IP가 이 대역에 속하는지 바로 확인할 수 있습니다
if target_ip in network:
    print(f"{target_ip}는 {network} 대역에 포함되어 있습니다.")
else:
    print(f"{target_ip}는 {network} 대역에 포함되어 있지 않습니다.")

'''
**문제 2**  — 위에서 만든 `log_analyzer.py` 모듈을 `import`해서, `WARNING` 레벨 로그만 필터링해 출력하는 코드를 작성해 봅시다.

```jsx
logs = [
    "[2026-05-06 12:01:22][INFO] Service started.",
    "[2026-05-06 12:01:27][WARNING] Low disk space.",
]
```
'''
from Ex04_log_analyzer import LogAnalyzer

logs = [
    "[2026-05-06 12:01:22][INFO] Service started.",
    "[2026-05-06 12:01:27][WARNING] Low disk space.",
]

logAnalyzer = LogAnalyzer(logs)

print(logAnalyzer.filter_by_level("WARNING"))


'''
**문제 3** — `from module import *`를 실무에서 지양해야 하는 이유와, 그 대안이 무엇인지 설명해 봅시다.

- from module import *은 불필요한 이름까지 가져와서 이름 충돌과 가독성 저하가 발생할 수 있기 때문에 지양합니다. 대신 필요한 것만 명시적으로 import하거나 import module 방식으로 사용하는 것이 좋습니다.

- from math import *처럼 *로 모든 것을 한 번에 가져오는 방식은 서로 다른 모듈이 같은 이름의 함수·변수를 가지고 있을 때 어떤 것이 실제로 쓰이는지 알 수 없게 만들어 실무에서는 지양됩니다. 
필요한 이름만 명시적으로 from 모듈명 import 이름1, 이름2 형태로 가져오는 것이 안전합니다.
'''






'''
### 📝 연습문제 — FTP 자동화

**문제 1**  — `FTP()` 객체로 `127.0.0.1`, 포트 `2121`에 접속해 로그인 성공 메시지를 출력하는 코드를 작성해 봅시다.
'''


'''
**문제 2** — `storbinary()`를 이용해 `firewall_rules.conf`라는 로컬 파일을 서버로 업로드하는 코드를 작성해 봅시다.
'''






'''
### 📝 연습문제 — 웹 스크래핑

**문제 1** — `requests.get()`에 `headers={'User-Agent': 'Mozilla/5.0'}`를 넣어 요청하고, `status_code`가 200인지 확인하는 코드를 작성해 봅시다.
'''


'''
**문제 2** — `soup.select(".news_txt")`로 뉴스 제목 태그를 모두 가져와, 그중 상위 3개의 텍스트만 리스트로 만드는 코드를 작성해 봅시다.
'''






'''
### 📝 연습문제 — 이메일 자동화

**문제 1**  — `MIMEText("서버 점검이 완료되었습니다.", 'plain')`로 텍스트 메시지 객체를 만들고 내용을 확인하는 코드를 작성해 봅시다.
'''


'''
**문제 2**  — `MIMEMultipart()`로 제목·발신자·수신자를 설정하고, HTML 본문을 `attach()`로 붙이는 코드를 작성해 봅시다.
'''






'''
### 📝 연습문제 — 엑셀 자동화

**문제 1**   — `Workbook()`으로 워크북을 만들고, `ws.append(["IP", "위험도", "차단여부"])`로 헤더를 추가한 뒤 저장하는 코드를 작성해 봅시다.
'''



'''
**문제 2**  — `firewall_logs = [("203.0.113.55", "High"), ("10.0.0.5", "Normal")]` 데이터를 순회하며 엑셀에 한 행씩 추가하고, 위험도가 `"High"`인 행의 글씨만 빨간색·굵게 처리하는 코드를 작성해 봅시다.
'''






'''
### 📝 연습문제 — 스케줄링

**문제 1**   — `datetime.now().strftime()`으로 현재 시각을 `"YYYYMMDD_HHMMSS"` 형태의 문자열로 변환하는 코드를 작성해 봅시다.
'''


'''
**문제 2** — `schedule.every().day.at("18:00").do(job)` 형태로, 매일 저녁 6시에 `job`이라는 함수를 실행하도록 예약하고 `run_pending()` 루프까지 포함한 코드를 작성해 봅시다.
'''


'''
**문제 3**  — `schedule.run_pending()`을 감싸는 `while` 루프에 `time.sleep(1)`을 꼭 넣어야 하는 이유를 설명해 봅시다.
'''