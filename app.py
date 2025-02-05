import streamlit as st
import pandas as pd
from PIL import Image
from ui.breed import run_breed
from ui.home import run_home
from ui.breed import train_knn_model
from sklearn.preprocessing import LabelEncoder

def load_data():
    df = pd.read_csv('dog/dogs-ranking-dataset.csv')
    
    df.loc[df['크기'] == 'small','크기'] = 1
    df.loc[df['크기'] == 'medium','크기'] = 2
    df.loc[df['크기'] == 'large','크기'] = 3

    # 문자열 데이터를 수치형으로 변환(지능)
    label_encoders = {}
    for col in ['지능'] :
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])
        label_encoders[col] = le
    return df, label_encoders

    

df, labal_encoders = load_data()


def main():
    st.dataframe(df)
    st.title("반려견 정보 대시보드 🐶")

    menu = ['Home', '사용자 입력 기반 품종 추천', '가격, 건강, 수명 예측']
    choice = st.sidebar.selectbox('메뉴', menu)

    if choice == menu[0]:
        run_home()
    elif choice == menu[1]:
        run_breed()
    
    
    



if __name__ == '__main__':
    main()