import streamlit as st
from ui.dev_progress import run_dev_progress
from ui.breed import run_breed
from ui.dog_find import run_bog_find
from ui.dog_predict import run_prediction
from ui.home import run_home





st.set_page_config(page_title="Dog Breed App", layout="wide")
    
st.markdown(
    """
    <style>
    /* 버튼 기본 스타일 */
        div.stButton > button {
            background-color: #FFCC80; /* 파스텔톤 주황 */
            color: #5A3E36; /* 부드러운 갈색 (텍스트) */
            font-size: 16px;
            font-weight: bold;
            border-radius: 10px;
            padding: 12px 24px;
            border: none;
            transition: all 0.3s ease-in-out;
        }

        /* 버튼 마우스 호버 효과 */
        div.stButton > button:hover {
            background-color: #FFB74D; /* 살짝 진한 주황 */
            transform: scale(1.05);
            box-shadow: 0px 4px 10px rgba(255, 179, 71, 0.3);
        }

        /* 버튼 클릭 효과 */
        div.stButton > button:active {
            background-color: #FFA726; /* 더 진한 주황 */
            transform: scale(0.98);
        }
        /* 배경색 설정 */
        .stApp {
            background-color: #fdf6e3; /* 연한 회색 */
        }
        /* 컨텐츠 정렬 */
        .block-container {
            max-width: 1000px; /* 중앙 정렬을 위한 최대 너비 */
            margin: auto;
            padding: 2rem;
            border-radius: 10px;
            background-color: white; /* 컨텐츠 부분만 흰색 */
            box-shadow: 2px 2px 10px rgba(0,0,0,0.1); /* 살짝 그림자 효과 */
        }

        /* 제목 스타일 */
        h1, h2, h3 {
            color: #343a40; /* 다크 그레이 */
        }
    </style>
    """,
    unsafe_allow_html=True
)

def main():
          

    tab1, tab2, tab3, tab4, tab5 = st.tabs(["🏠 홈", "🚀 개발 과정","🐕 강아지 추천", "📈 데이터 분석", "🔍품종 찾기"])

    with tab1:
        st.title("🐾강아지 정보 & AI 추천 대시보드")
        run_home()
    with tab2:
        st.subheader("🚀 개발 과정")
        run_dev_progress()
    with tab3:
        st.subheader("🐕 강아지 추천 기능")
        run_breed()
    with tab4:
        st.subheader("📈 데이터 분석")
        run_prediction()
    with tab5:
        st.subheader("🔍 품종 찾기")
        run_bog_find()



    
    



if __name__ == '__main__':
    main()