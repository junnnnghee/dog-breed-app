import streamlit as st
import base64

def set_bg(image_path):
    """배경 이미지를 왼쪽 상단에 고정하는 함수"""
    with open(image_path, "rb") as f:
        encoded_image = base64.b64encode(f.read()).decode()

    bg_image = f"""
    <style>
    body {{
        background: url("data:image/png;base64,{encoded_image}") no-repeat left top fixed;
        background-size: auto 100vh;  /* 높이에 맞게 조정 */
    }}
    
    .stApp {{
        background: none !important;  /* 기본 배경 제거 */
    }}
    
    /* 데이터 출력 부분을 흰색 박스로 지정 */
    .block-container {{
        background-color: rgba(255, 255, 255, 0.8);
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
    }}
    </style>
    """
    st.markdown(bg_image, unsafe_allow_html=True)