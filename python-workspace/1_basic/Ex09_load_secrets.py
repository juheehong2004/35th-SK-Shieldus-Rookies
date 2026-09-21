import os
from dotenv import load_dotenv

# .env 파일의 환경변수들을 시스템 환경변수(os.environ)로 로드
load_dotenv()

# **.env 파일에서** VT_API_KEY와 AUDIT_TARGET_HOST 값을 가져옴
vt_key = os.getenv("VT_API_KEY")
target_host = os.getenv("AUDIT_TARGET_HOST") # 없으면 컴퓨터에

# 가져온 환경변수 출력
print(f"이번 감사 대상 호스트: {target_host}")
# API 키의 보안을 위해 앞 4자리만 출력하고 나머지는 마스킹(****) 처리
print(f"스캐너 키 로드 확인: {vt_key[:4]}****")

# ------------------------------------------------------------------
# [케이스 1] .env에 존재하지 않는 환경변수를 불러온 후 슬라이싱할 경우
# ------------------------------------------------------------------
## os.getenv("VT_KEY")는 키가 존재하지 않으면 None을 반환함
# vt_key_none = os.getenv("VT_KEY")

## NoneType 객체는 슬라이싱([:4])을 지원하지 않으므로 TypeError 발생!
## TypeError: 'NoneType' object is not subscriptable
# print(f"스캐너 키 로드 확인: {vt_key_none[:4]}****")


# ------------------------------------------------------------------
# [케이스 2] .env에 존재하지 않을 경우를 대비해 기본값(Default) 지정하기 (env 파일에 있는지 없는지 모르는 경우도 있음)
# ------------------------------------------------------------------
## 환경변수 "VT_KEY"가 없을 경우 두 번째 인자인 'test-0000-0000-key'를 기본값으로 사용
vt_key_none = os.getenv("VT_KEY", 'test-0000-0000-key')

## 기본값이 문자열이므로 슬라이싱([:4]) 시 오류 없이 'test'만 추출됨 -> "test****" 출력
print(f"스캐너 키 로드 확인: {vt_key_none[:4]}****")