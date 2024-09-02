import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np

def create_carbon_footprint_gauge(value):
    """탄소 발자국을 게이지 차트로 표시합니다."""
    fig = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = value,
        domain = {'x': [0, 1], 'y': [0, 1]},
        title = {'text': "탄소 발자국 (톤 CO2e/년)"},
        gauge = {
            'axis': {'range': [None, 10], 'tickwidth': 1, 'tickcolor': "darkblue"},
            'bar': {'color': "darkblue"},
            'steps': [
                {'range': [0, 2], 'color': "cyan"},
                {'range': [2, 5], 'color': "royalblue"},
                {'range': [5, 8], 'color': "lightcoral"},
                {'range': [8, 10], 'color': "red"}],
            'threshold': {
                'line': {'color': "red", 'width': 4},
                'thickness': 0.75,
                'value': 9}}))
    st.plotly_chart(fig)

def create_carbon_trend_chart(data):
    """탄소 발자국 트렌드를 라인 차트로 표시합니다."""
    df = pd.DataFrame(data, columns=['date', 'footprint'])
    fig = px.line(df, x='date', y='footprint', title='탄소 발자국 추이')
    fig.update_traces(mode='lines+markers')
    st.plotly_chart(fig)

def create_category_breakdown(data):
    """카테고리별 탄소 발자국 비율을 선버스트 차트로 표시합니다."""
    fig = px.sunburst(data, path=['category', 'subcategory'], values='value',
                      title='카테고리별 탄소 발자국 비율')
    st.plotly_chart(fig)

def create_reduction_potential_chart(data):
    """절감 잠재량을 워터폴 차트로 표시합니다."""
    fig = go.Figure(go.Waterfall(
        name = "20", orientation = "v",
        measure = ["relative", "relative", "relative", "total"],
        x = ["교통", "에너지", "식습관", "총 절감 잠재량"],
        textposition = "outside",
        text = ["+2.5", "+3.2", "+1.8", "7.5"],
        y = [2.5, 3.2, 1.8, 0],
        connector = {"line":{"color":"rgb(63, 63, 63)"}},
    ))
    fig.update_layout(title = "탄소 절감 잠재량 분석", showlegend = False)
    st.plotly_chart(fig)

# Streamlit 앱에서 사용 예시
create_carbon_footprint_gauge(6.7)

trend_data = {'date': pd.date_range(start="2024-01-01", end="2024-12-31", freq="M"),
              'footprint': np.cumsum(np.random.normal(0.1, 0.02, 12))}
create_carbon_trend_chart(trend_data)

category_data = pd.DataFrame([
    {'category': '교통', 'subcategory': '자동차', 'value': 2.5},
    {'category': '교통', 'subcategory': '대중교통', 'value': 0.8},
    {'category': '에너지', 'subcategory': '전기', 'value': 1.5},
    {'category': '에너지', 'subcategory': '가스', 'value': 1.0},
    {'category': '식습관', 'subcategory': '육류', 'value': 1.2},
    {'category': '식습관', 'subcategory': '채소', 'value': 0.3},
])
create_category_breakdown(category_data)

create_reduction_potential_chart({})  # 데이터는 함수 내에서 하드코딩됨