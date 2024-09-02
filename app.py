import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from datetime import datetime, timedelta
# 새로운 import 문 추가
from ai_integration import get_ai_recommendation, analyze_carbon_trend
from visualizations import (create_carbon_footprint_gauge, create_carbon_trend_chart,
                            create_category_breakdown, create_reduction_potential_chart)

# 페이지 설정
st.set_page_config(page_title="개인 탄소 발자국 거래 시스템", layout="wide")

# 세션 상태 초기화 함수
def initialize_session_state():
    if 'carbon_credits' not in st.session_state:
        st.session_state.carbon_credits = 4.0  # 초기 할당량
    if 'virtual_trees' not in st.session_state:
        st.session_state.virtual_trees = 0
    if 'challenges' not in st.session_state:
        st.session_state.challenges = []

# 실시간 탄소 발자국 시뮬레이션 함수
@st.cache_data
def simulate_real_time_footprint():
    now = datetime.now()
    times = [now - timedelta(minutes=i) for i in range(60, 0, -1)]
    footprints = np.cumsum(np.random.normal(0.001, 0.0005, 60))
    return pd.DataFrame({'time': times, 'footprint': footprints})

def main():
    initialize_session_state()

    # 사이드바 - 네비게이션
    page = st.sidebar.selectbox("페이지 선택", ["홈", "탄소 크레딧 관리", "마켓플레이스", "프로필"])

    if page == "홈":
        st.title("내 탄소 발자국")
        
        # 현재 탄소 발자국 상태
        current_footprint = st.session_state.carbon_credits
        st.metric(label="현재 탄소 크레딧", value=f"{current_footprint:.2f} 톤", delta=f"{4.0 - current_footprint:.2f} 톤")
        
        # 새로운 기능: 탄소 발자국 게이지
        create_carbon_footprint_gauge(current_footprint)
        
        # 탄소 발자국 그래프
        trend_data = {'date': pd.date_range(start="2024-01-01", end="2024-12-31", freq="M"),
                      'footprint': np.cumsum(np.random.normal(0.1, 0.02, 12))}
        create_carbon_trend_chart(trend_data)
        
        # 가상 나무
        st.subheader(f"당신의 가상 숲: {st.session_state.virtual_trees} 그루")
        if st.button("나무 심기"):
            if st.session_state.carbon_credits >= 0.1:
                st.session_state.carbon_credits -= 0.1
                st.session_state.virtual_trees += 1
                st.success("가상 나무를 1그루 심었습니다!")
            else:
                st.error("탄소 크레딧이 부족합니다.")
        
        # 새로운 기능: AI 추천
        user_data = {"transport": "car", "energy_usage": "high", "diet": "meat-heavy"}
        if st.button("AI 추천 받기"):
            recommendation = get_ai_recommendation(user_data)
            st.write(recommendation)
        
        # 새로운 기능: 카테고리별 분석
        category_data = pd.DataFrame([
            {'category': '교통', 'subcategory': '자동차', 'value': 2.5},
            {'category': '교통', 'subcategory': '대중교통', 'value': 0.8},
            {'category': '에너지', 'subcategory': '전기', 'value': 1.5},
            {'category': '에너지', 'subcategory': '가스', 'value': 1.0},
            {'category': '식습관', 'subcategory': '육류', 'value': 1.2},
            {'category': '식습관', 'subcategory': '채소', 'value': 0.3},
        ])
        create_category_breakdown(category_data)
        
        # 새로운 기능: 절감 잠재량 분석
        create_reduction_potential_chart({})
        
        # 새로운 기능: 탄소 발자국 트렜드 분석
        carbon_data = [2.5, 2.3, 2.7, 2.4, 2.2]  # 최근 5일간의 가상 데이터
        if st.button("탄소 발자국 트렌드 분석"):
            analysis = analyze_carbon_trend(carbon_data)
            st.write(analysis)

    elif page == "탄소 크레딧 관리":
        st.title("탄소 크레딧 관리")
        # (기존 코드 유지)

    elif page == "마켓플레이스":
        st.title("탄소 크레딧 마켓플레이스")
        # (기존 코드 유지)

    elif page == "프로필":
        st.title("내 프로필")
        # (기존 코드 유지)

    # AI 기반 예측 및 추천 (사이드바)
    st.sidebar.subheader("AI 추천")
    if st.sidebar.button("탄소 절감 팁 받기"):
        tips = [
            "대중교통을 이용하세요.",
            "전기 절약을 위해 사용하지 않는 전자기기의 플러그를 뽑으세요.",
            "일회용품 사용을 줄이고 재사용 가능한 제품을 사용하세요.",
            "육류 소비를 줄이고 채식 위주의 식단을 시도해보세요.",
            "에너지 효율이 높은 가전제품을 사용하세요."
        ]
        st.sidebar.info(np.random.choice(tips))

    # 실시간 탄소 발자국 시뮬레이션 (사이드바)
    st.sidebar.subheader("실시간 탄소 발자국")
    real_time_data = simulate_real_time_footprint()
    fig = px.line(real_time_data, x='time', y='footprint', title='최근 1시간 탄소 발자국')
    st.sidebar.plotly_chart(fig, use_container_width=True)

if __name__ == "__main__":
    main()