class BaseServer:
    def __init__(self, name: str, ip: str):
        self.name = name   # 관리용 이름
        self.ip = ip        # 접속용 IP
        self.status = "Unknown"

    def power_on(self):
        print(f"{self.name} 서버 전원 켜기")
        self.status = "Running"

    def power_off(self):
        print(f"{self.name} 서버 전원 끄기")
        self.status = "Stopped"

    def check(self):
        print(f"{self.name} 서버 점검...")


class WebServer(BaseServer):
    def run_service(self):
        print("웹 서비스(80/443) 가동!")

    def check(self):
        # 부모의 기능을 재정의(override) - 웹 서버만의 특별한 점검
        print(f"{self.name} 웹 서버만의 특별한 점검 (80/443 응답 확인)...")


# 여기
my_web = WebServer("Web-01", "192.168.19.2")
# 부모꺼 
my_web.power_on()# Web-01 서버 전원 켜기
# 내꺼
my_web.run_service() # 웹 서비스(80/443) 가동!
# 부모+나 둘다 갖고있음(오버라이딩) => 자식 메소드 호출
my_web.check() # Web-01 웹 서버만의 특별한 점검 (80/443 응답 확인)...