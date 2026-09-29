'''
#### [ 도전 문제 2-A ]

### 문제 2-A. pathlib로 폴더·파일 생성 및 확인

os 모듈은 사용하지 않고, pathlib만 사용해 아래 순서대로 동작하는 코드를 작성하세요.

1. reports/2026/09 폴더를 생성한다 (이미 존재해도 오류 없이)
2. 해당 폴더 안에 scan_result.txt 파일을 생성하고 "Scan completed: 3 hosts checked" 내용을 저장한다
3. 파일이 존재하는지 확인 후, 존재하면 "✅ 파일 확인: <파일명>" 형태로 출력한다
4. 파일 크기(bytes)도 함께 출력한다

```jsx
from pathlib import Path

# 여기에 작성하세요

```

기대 출력:
✅ 파일 확인: scan_result.txt
파일 크기: 35 bytes

💡 힌트: 파일 크기는 Path 객체의 .stat().st_size 속성으로 구합니다.
'''






'''
#### [ 도전 문제 2-B]

### 문제 2-B. glob + shutil 파일 아카이빙

시나리오: 현재 폴더의 .log 파일을 archive/ 폴더에 복사하고, 복사가 끝난 원본 파일 이름을 "파일명_done.log" 형태로 변경하세요.

```jsx
from pathlib import Path
import shutil

# 준비: 샘플 로그 파일 3개 생성
for name in ["access.log", "error.log", "auth.log"]:
    Path(name).write_text(f"{name} 내용", encoding="utf-8")

# 1. 현재 폴더의 모든 .log 파일 목록 가져오기 (glob)
log_files = _______________

# 2. archive 폴더 생성 (없으면)
_______________

# 3. 각 파일을 archive/ 폴더에 복사 후, 원본 파일 이름 변경
for log in log_files:
    shutil.copy(_______________)            # 복사
    new_name = _______________              # 예: access.log → access_done.log
    log.rename(_______________)             # 이름 변경

# 4. 결과 확인 출력
for f in Path("archive").iterdir():
    print(f"[archive] {f.name}")

for f in Path(".").glob("*_done.log"):
    print(f"[완료] {f.name}")
```

기대 출력:
[archive] access.log
[archive] error.log
[archive] auth.log
[완료] access_done.log
[완료] error_done.log
[완료] auth_done.log

💡 힌트: 파일 stem 속성은 확장자를 뺀 이름만 반환합니다. (예: Path("access.log").stem → "access")
'''
