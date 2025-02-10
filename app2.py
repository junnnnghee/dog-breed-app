import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestRegressor

# 데이터 로드 및 모델 훈련 (이미 훈련된 모델 사용)
dog_data = pd.read_csv('dog_data.csv')
# 여기서 모델을 훈련하고, 사용자가 입력한 데이터를 예측하는 로직을 작성

# 스트림릿 UI
st.title('반려견 입양 추천 앱')

# 사용자 입력 받기
st.sidebar.header('입력 항목')
size = st.sidebar.selectbox('크기 선택', ['small', 'medium', 'large'])
intelligence = st.sidebar.slider('지능 수준', 1, 5, 3)
children_friendly = st.sidebar.selectbox('어린이 적합성', ['Yes', 'No', 'With Training'])
disease = st.sidebar.selectbox('선천적 질병', ['none', 'lion jaw', 'hip problems'])

# 추천 품종 (예시)
st.subheader('추천 품종')
# 품종 추천 로직
recommended_breeds = ['Border Terrier', 'Cairn Terrier', 'Siberian Husky']  # 예시로 제공
st.write(f"추천 품종: {', '.join(recommended_breeds)}")

# 건강 정보
st.subheader('품종 건강 정보')
selected_breed = st.selectbox('추천 품종 선택', recommended_breeds)
if selected_breed == 'Border Terrier':
    st.write("선천적 질병: none, 유전적 질병: low, 수명: 14년")
elif selected_breed == 'Cairn Terrier':
    st.write("선천적 질병: 'lion jaw', heart problems, 유전적 질병: moderate, 수명: 13.5년")
elif selected_breed == 'Siberian Husky':
    st.write("선천적 질병: none, 유전적 질병: moderate, 수명: 12.5년")

# 가격 예측
st.subheader('예상 가격 예측')
# 예시로 예상 가격을 제공
predicted_price = 3000000  # 예시 가격
st.write(f"예상 입양 가격: {predicted_price} 원")

# 성격 정보
st.subheader('성격 정보')
if selected_breed == 'Border Terrier':
    st.write("성격: 활발하고 충성스러우며, 가족과 잘 어울립니다.")
elif selected_breed == 'Cairn Terrier':
    st.write("성격: 용감하고 독립적이며, 활동적입니다.")
elif selected_breed == 'Siberian Husky':
    st.write("성격: 에너지가 넘치며 독립적이고 충성스럽습니다.")