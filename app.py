import streamlit as st
import pandas as pd
from PIL import Image

def main():
    st.title('🐶강아지 정보 앱🐶💓')
    st.subheader('강아지에 대한 정보를 제공하는 앱입니다.')
    st.markdown("귀여운 강아지들을 만나보세요! 💕")

    main_image = Image.open('./image/dogkind.webp')
    st.image(main_image, width=500)
    
<<<<<<< HEAD
    df = pd.read_csv('dog/Car_Purchasing_Data.csv')
    print(df)
    st.dataframe(df)
    
=======
    
    menu = ['홈', '품종 정보']
    st.sidebar.title('메뉴')
    st.sidebar.text('메뉴를 선택하세요.')
    st.sidebar.button('홈')
    st.sidebar.button('품종 정보')


        

>>>>>>> 2508f305fe9fc43edbc3f6741e66ffe0a6440c00



if __name__ == '__main__':
    main()