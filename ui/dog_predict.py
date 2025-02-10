from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import streamlit as st
import pandas as pd


def run_prediction():
    df = pd.read_csv('dog_data.csv')
    
    reg_models = train_regression_models(df)

    
    st.header("💰 건강, 가격, 수명 예측")
    selected_breed = st.selectbox("예측할 품종 선택", df["품종"].unique())
    breed_data = df[df["품종"] == selected_breed][["크기", "지능", "어린이 적합성"]].values
    
    predicted_price = reg_models["평균구매가격"].predict(breed_data)[0]
    predicted_health = reg_models["유전적 질병의 수"].predict(breed_data)[0]
    predicted_lifespan = reg_models["수명(년)"].predict(breed_data)[0]
    
    st.write(f"### 💲 예상 가격: ${predicted_price:,.2f}")
    st.write(f"### 🏥 예상 건강 문제 수: {predicted_health:.2f}개")
    st.write(f"### ⏳ 예상 수명: {predicted_lifespan:.1f}년")
    

def train_regression_models(df):
    models = {}
    target_columns = ["평균구매가격", "유전적 질병의 수", "수명(년)"]
    features = ["크기", "지능", "어린이 적합성"]
    
    for target in target_columns:
        X = df[features]
        y = df[target]
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        model = LinearRegression()
        model.fit(X_train, y_train)
        models[target] = model
    
    return models    