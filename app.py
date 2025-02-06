import streamlit as st
import pandas as pd
from PIL import Image
from ui.breed import run_breed
from ui.home import run_home
from ui.breed import train_knn_model
from sklearn.preprocessing import LabelEncoder
from ui.breed import load_data



def main():
    

    menu = ['Home', '사용자 입력 기반 품종 추천', '가격, 건강, 수명 예측']
    choice = st.sidebar.selectbox('메뉴', menu)

    if choice == menu[0]:
        run_home()
    elif choice == menu[1]:
        run_breed()
    
    
    



if __name__ == '__main__':
    main()