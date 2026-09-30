class Server:
    def __init__(self, name, ip):
        self.name = name
        self.ip = ip

    def info(self):
        # self가 있어야 '자신'의 name, ip를 꺼내올 수 있습니다
        print(f"자신의 이름: {self.name}, 주소: {self.ip}")


# 여기
web_svr = Server("WEB-01", "192.168.1.2")
web_svr.info()