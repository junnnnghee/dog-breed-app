from sklearn.calibration import LabelEncoder
import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier


def load_data():
    df = pd.read_csv('dog/dogs-ranking-dataset.csv')
    
    # 데이터 전처리
    df = df.dropna()  # 결측값 제거
    
    # 문자열 데이터를 수치형으로 변환
    label_encoders = {}
    for col in ["size.1", "intelligence"]:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])
        label_encoders[col] = le
    
    return df, label_encoders

    

def run_breed():
    st.subheader('품종을 추천해드립니다.')

    df = pd.read_csv('dog/dogs-ranking-dataset.csv',encoding='utf-8')

    df.loc[df['크기'] == 'small','크기'] = 1
    df.loc[df['크기'] == 'medium','크기'] = 2
    df.loc[df['크기'] == 'large','크기'] = 3

    st.text('아래는 개 품종 순위 Top5 정보입니다.')
    st.dataframe(df.head())

       
    



    st.text('원하는 개의 사이즈, 지능, 아이들과의 적합성 점수를 선택하세요.')
    
    
    st.slider('사이즈', min_value=1, max_value=3)

    st.text('지능')
    st.radio('지능을 선택하세요.', list(sorted(df['지능'].unique())))

    어린이적합성_list = ['높음', '중간', '낮음']
    st.radio('어린이 적합성을 선택하세요.', 어린이적합성_list)

def train_knn_model(df):
        
    y = df['품종']
    X = df.loc[ : , ['크기', '지능', '어린이 적합성'] ]

    breed_encoder = LabelEncoder()
    y = sorted(breed_encoder.fit_transform(y))

    intelligence_encoder = LabelEncoder()
    X['지능'] = intelligence_encoder.fit_transform(X['지능'])

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    knn = KNeighborsClassifier(n_neighbors=5)
    knn.fit(X_train, y_train)

    st.da(knn)

