import requests

# response = requests.get("https://google.com")
# print(response.text)

response = requests.get("https://api.ipify.org?format=json", timeout=5)
if response.status_code == 200:
    data = response.json()
    print(data)
    print(f"현재 서버의 공인 IP: {data['ip']}")
else:
    print(f"연결 실패: {response.status_code}")