import streamlit as st
import pandas as pd

def main():
    st.title('강아지 정보 앱')
    st.subheader('강아지에 대한 정보를 제공하는 앱입니다.')
    st.text('메뉴를 선택해주세요.')
    
    df = pd.read_csv('dog/Car_Purchasing_Data.csv')
    print(df)
    st.dataframe(df)
    



if __name__ == '__main__':
    main()