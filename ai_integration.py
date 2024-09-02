import os
from anthropic import Anthropic, HUMAN_PROMPT, AI_PROMPT

# API 키 가져오기
ANTHROPIC_API_KEY = os.getenv('ANTHROPIC_API_KEY')
if not ANTHROPIC_API_KEY:
    raise ValueError("ANTHROPIC_API_KEY 환경 변수가 설정되지 않았습니다.")

anthropic = Anthropic(api_key=ANTHROPIC_API_KEY)

def get_ai_recommendation(user_data):
    prompt = f"{HUMAN_PROMPT} 다음은 사용자의 탄소 발자국 데이터입니다: {user_data}. 이 사용자에게 탄소 발자국을 줄일 수 있는 개인화된 조언을 제공해주세요.{AI_PROMPT}"
    
    response = anthropic.completions.create(
        model="claude-3-sonnet-20240229",
        prompt=prompt,
        max_tokens_to_sample=300,
    )
    return response.completion

def analyze_carbon_trend(carbon_data):
    prompt = f"{HUMAN_PROMPT} 다음은 사용자의 최근 탄소 발자국 데이터입니다: {carbon_data}. 이 데이터의 트렌드를 분석하고, 주요 인사이트를 제공해주세요.{AI_PROMPT}"
    
    response = anthropic.completions.create(
        model="claude-3-sonnet-20240229",
        prompt=prompt,
        max_tokens_to_sample=400,
    )
    return response.completion

# Streamlit 앱에서 사용 예시
if st.button("AI 추천 받기"):
    user_data = {"transport": "car", "energy_usage": "high", "diet": "meat-heavy"}
    recommendation = get_ai_recommendation(user_data)
    st.write(recommendation)

if st.button("탄소 발자국 트렌드 분석"):
    carbon_data = [2.5, 2.3, 2.7, 2.4, 2.2]  # 최근 5일간의 가상 데이터
    analysis = analyze_carbon_trend(carbon_data)
    st.write(analysis)