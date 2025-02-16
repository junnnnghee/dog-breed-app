import streamlit as st

from ui.breed import run_breed


def run_home():
    
    col1, col2 = st.columns([3, 2])  # 비율 조절 (텍스트 3, 이미지 2)
    with col1:
        st.write("#### 🔍 반려견을 찾고 계신가요?")  
        st.write("""
            이 앱에서는 **당신에게 딱 맞는 강아지 품종을 추천**하고,  
            **강아지의 가격, 건강, 수명 예측 기능**을 제공합니다!  
            
            원하는 정보를 쉽게 찾아보세요! 🐾
        """)
    with col2:
        st.image("image/dog_img.png", width=300)

    st.divider()  # 탭과 콘텐츠 구분선

    st.write("## 📌 주요 기능")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🐕 강아지 추천 기능")
        st.write("원하는 강아지의 특성을 선택하면, 가장 적합한 품종을 추천해 드립니다.")
        

    with col2:
        st.subheader("📊 데이터 분석 기능")
        st.write("강아지 품종 데이터를 분석하여 다양한 인사이트를 제공합니다.")
        st.write("📌 자세한 데이터 분석 과정은 **[데이터 분석 탭]**에서 확인할 수 있습니다.")
        

    st.divider()  # 탭과 콘텐츠 구분선

    
    # 안내 메시지
    st.info("📌 상단의 메뉴 탭을 클릭하세요!")
