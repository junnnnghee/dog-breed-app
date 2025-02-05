import streamlit as st
import pandas as pd
from PIL import Image
from ui.breed import run_breed
from ui.home import run_home

def main():
    st.title("반려견 정보 대시보드 🐶")

    menu = ['Home', '사용자 입력 기반 품종 추천', '가격, 건강, 수명 예측']
    choice = st.sidebar.selectbox('메뉴', menu)

    if choice == menu[0]:
        run_home()
    elif choice == menu[1]:
        run_breed()
    

    



if __name__ == '__main__':
    main()