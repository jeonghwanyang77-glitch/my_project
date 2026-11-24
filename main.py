# 대시보드 홈페이지
# 1. 모듈 가져오기
from fastapi import FastAPI, Request
# 백엔드 서버 구성시 템플릿엔진 사용 => 서버측에서 동적으로 html을 생성 응답 => SSR
# 파이썬 계열 주로 사용되는 템플릿엔진 jinja2 <= 웹, LLM 프롬포트 구성 사 => AI
# html 관여
from fastapi.templating import Jinja2Templates
# 정적 데이터 처리용 => ccs, js 관여
from fast.staticfiles import Staticfiles

# 2. Fastapi 앱 생성, 템플릿엔진, 정적데이터 처리 설정
app = fastAPI()
templates = Jinja2Templates(directory="templates") # 특정 위치를 지정할 수 있다
# 정적 데이터의 위치, url 표기법 설정
app.mount("/static", Staticfiles(directory="static"), name="static")

# 3. 라우팅 구성/정의

# 4. 서버가동 => 명령어 대체