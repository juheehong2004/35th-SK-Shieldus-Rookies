class BaseServer:
    def __init__(self, name, ip):
        self.name = name
        self.ip = ip

    def check(self):
        pass

class WebServer(BaseServer):
    def run_service(self):
        pass

web = WebServer("WEB-01", "192.168.1.10")

# dir() : 이 객체가 어떤 속성/메서드를 갖고 있는지 리스트로 확인
# 처음 보는 객체(예: 팀 동료가 만든 클래스, 외부 SDK 객체)를 다룰 때 자주 사용합니다
print(dir(web))
# ['__class__', ..., 'check', 'ip', 'name', 'run_service']