'''
[파이썬 PBL 기본-2] 인프라 취약점 로그 자동 아카이빙 및 리포팅
'''

from pathlib import Path
import shutil
import glob
import csv
import json

# 1. 사전 준비
# 실무형 취약점 스캔 로그 데이터 생성
log_data = """Scan Time: 2026-09-07 02:00:11
Target: 10.0.2.15
Port: 21 STATUS: OPEN
Port: 22 STATUS: OPEN
Port: 443 STATUS: OPEN
Port: 3389 STATUS: OPEN
Port: 80 STATUS: OPEN
Port: 8080 STATUS: OPEN"""

LOG_FILE = Path("vuln_scan.log") # 스캐너가 생성하는 원본 로그

LOG_FILE.write_text(log_data, encoding="utf-8")
print("✅ 취약점 스캔 로그(vuln_scan.log) 생성 완료!")

# 2. 로그 아카이빙
ARCHIVE_DIR = Path("archive") # 원본 로그 보관 폴더

if LOG_FILE.exists(): # 현재 폴더에 원본 로그 파일이 존재하는지 확인
    # archive 폴더가 없으면 생성
    ARCHIVE_DIR.mkdir(exist_ok=True)
    # 원본 로그 파일을 archive 폴더로 이동
    shutil.move(str(LOG_FILE), str(ARCHIVE_DIR / LOG_FILE.name))
    print(f"로그 아카이빙 완료: {LOG_FILE.name} 파일을 {ARCHIVE_DIR.name} 폴더로 이동했습니다.")

# 3. 파싱 & 필터링

# 안전 포트 판별 함수 - 수정 불가능한 튜플 사용
def is_safe_port(port):
    """
    사내 보안 정책상 '안전 포트'로 등록된 포트인지 확인한다.
    화이트리스트는 수정이 불가능한 튜플(Tuple)로 관리하여 실수로 변경되는 것을 막는다.
 
    Args:
        port (int): 점검할 포트 번호
    Returns:
        bool: 안전 포트이면 True, 아니면 False
    """
    safe_ports = (22, 80, 443)

    return port in safe_ports


log_path = ARCHIVE_DIR / LOG_FILE.name
ports = []

if log_path.exists():
    with open(log_path, "r", encoding="utf-8") as file:        
        for line in file:
            if line.startswith("Port: "):
                words = line.split(" ")
                if len(words) >= 2:
                    ports.append(int(words[1]))


unsafe_ports = list(filter(lambda port: not is_safe_port(port), ports))

print(f"안전 포트 미등록 포트: {unsafe_ports}")

# 파일 검색 확인
log_files = glob.glob(str(ARCHIVE_DIR / "*.log"))
print("archive 폴더 내 .log 파일 목록")
for path in log_files:
    print(f"   - {path}")


# 4. 파일 저장 (다중 포맷 리포팅)
CSV_FILE = Path("vulnerable_ports.csv")
JSON_FILE = Path("vulnerability_alert.json")

# CSV 파일에 저장 (헤더: Detected_Port, Severity / 값은 "Critical" 고정)
with open(CSV_FILE, "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["Detected_Port", "Severity"])
    writer.writeheader()
    for port in unsafe_ports:
        writer.writerow({"Detected_Port": port, "Severity": "Critical"})
print(f"CSV 파일로 저장 완료: {CSV_FILE}")


# JSON 파일에 저장 (들여쓰기 4칸, Assigned_Engineer 필드를 None으로 설정하여 저장 시 null로 치환)
alert_data = {
    "Vulnerable_Ports": unsafe_ports,
    "Severity": "Critical",
    "Assigned_Engineer": None
}
 
with open(JSON_FILE, "w", encoding="utf-8") as file:
    json.dump(alert_data, file, indent=4)
print(f"JSON 파일로 저장 완료: {JSON_FILE}")

# JSON 파일에서 None이 null로 저장되었는지 확인
with open(JSON_FILE, "r", encoding="utf-8") as file:
    raw_text = file.read()
 
null_check = '"Assigned_Engineer": null' in raw_text
print(f"저장 시 Python None -> JSON null 변환되었는지 확인: {null_check}")