import streamlit as st
import pandas as pd

def main():
    st.title('강아지 정보 앱')
    st.subheader('강아지에 대한 정보를 제공하는 앱입니다.')
    
    menu = ['홈', '품종 정보']
    st.sidebar(menu)




if __name__ == '__main__':
    main()