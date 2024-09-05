from anthropic import Anthropic
from config import ANTHROPIC_API_KEY, AI_MODEL, MAX_TOKENS

# Anthropic 클라이언트 초기화
anthropic = Anthropic(api_key=ANTHROPIC_API_KEY)

def get_ai_recommendation(user_data):
    try:
        message = anthropic.messages.create(
            model=AI_MODEL,
            max_tokens=MAX_TOKENS,
            messages=[
                {"role": "user", "content": f"다음은 사용자의 탄소 발자국 데이터입니다: {user_data}. 이 사용자에게 탄소 발자국을 줄일 수 있는 개인화된 조언을 제공해주세요."}
            ]
        )
        return message.content
    except Exception as e:
        print(f"AI 추천을 가져오는 중 오류 발생: {str(e)}")
        return None

def analyze_carbon_trend(carbon_data):
    try:
        message = anthropic.messages.create(
            model=AI_MODEL,
            max_tokens=MAX_TOKENS,
            messages=[
                {"role": "user", "content": f"다음은 사용자의 최근 탄소 발자국 데이터입니다: {carbon_data}. 이 데이터의 트렌드를 분석하고, 주요 인사이트를 제공해주세요."}
            ]
        )
        return message.content
    except Exception as e:
        print(f"탄소 트렌드 분석 중 오류 발생: {str(e)}")
        return None