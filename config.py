import os
from dotenv import load_dotenv

# .env 파일에서 환경 변수 로드
load_dotenv()

# 환경 변수에서 API 키 가져오기
ANTHROPIC_API_KEY = os.getenv('ANTHROPIC_API_KEY')

# 기타 설정
DEBUG = os.getenv('DEBUG', 'False').lower() in ('true', '1', 't')
INITIAL_CARBON_CREDITS = 4.0
MAX_VIRTUAL_TREES = 100

# AI 모델 설정
AI_MODEL = "claude-3-sonnet-20240229"
MAX_TOKENS = 300

# 데이터베이스 설정 (향후 사용을 위해)
DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///carbon_footprint.db')

# 시각화 설정
CHART_COLORS = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']