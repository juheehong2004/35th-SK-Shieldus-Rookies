from pathlib import Path
import shutil

# 상황:
# 서버에서 생성된 보안 로그(security.log)를 백업 폴더에 복사하고,
# 원본 로그는 처리 완료 폴더로 이동하려고 합니다.


# 1. 준비 작업
# 현재 폴더에 "security.log" 파일이 있는지 확인하세요.
# 파일이 없다면 아래 내용을 가진 파일을 생성하세요.
#
# "Suspicious Login Detected"


# 2. 폴더 및 경로 준비
# "backup" 폴더와 "processed" 폴더를 사용할 예정입니다.
#
# backup 폴더 안에 "security_backup.log"라는 경로를 만드세요.


# 3. 파일 복사
# security.log 파일을 backup/security_backup.log로 복사하세요.
#
# 원본 security.log 파일은 유지되어야 합니다.


# 4. 파일 이동
# 원본 security.log 파일을 processed 폴더로 이동하세요.
#
# 이동 후 현재 폴더에는 security.log가 없어야 합니다.


# 5. 로그 파일 검색
# backup 폴더에서 확장자가 ".log"인 파일 목록을 glob()을 사용하여 출력하세요.


# 6. 파일 이름 변경
# backup/security_backup.log 파일이 존재한다면
# "backup_2026.log"로 이름을 변경하세요.


# 7. 최종 확인
# backup 폴더의 모든 파일 목록을 출력하세요.
# processed 폴더의 모든 파일 목록도 출력하세요.