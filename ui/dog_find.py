import streamlit as st
import pandas as pd

def run_bog_find():
    df = pd.read_csv('dog/dog_breeds_data.csv')
    

    
    col1, col2= st.columns([3, 2])
    with col1 :
        st.subheader("여러 품종의 정보를 확인해보세요!")
        st.write("""
            강아지 추천 탭에서 옵션을 선택해 품종 추천을 받았지만

            원하시는 품종이 아닐 수도 있습니다!
            
            그 외에 강아지를 알고싶으시다면 품종을 선택해서 확인해보세요!
            """)
    with col2 :
        st.image('image/img.png', width=300)

    st.divider()
    
    option = st.selectbox('품종 찾기', ['선택하세요'] + sorted(list(df['품종'].unique())))

    st.write("")

    if option != '선택하세요':
        breed_option = df[df['품종'] == option]
        breed_info = breed_option.iloc[ :, :-3]
        st.write("##### 📌 아래는 선택하신 품종의 특징, 수명, 등의 데이터입니다")
        st.dataframe(breed_info)

        breed_img = breed_option['이미지'].values[0]
        st.write("##### 📌 선택하신 품종의 이미지입니다")
        st.image(breed_img, width=400)

        breed_url = breed_option['정보링크'].values[0]
        st.write("##### 📌 자세한 정보를 알고싶다면 링크를 클릭하세요!")
        st.page_link(breed_url, label='웹사이트 방문하기', icon="🌍")

        
        


