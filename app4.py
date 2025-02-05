import streamlit as st
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LinearRegression

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

def train_knn_model(df):
    features = ["size.1", "intelligence", "score for kids"]
    X = df[features]
    y = df["Breed"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    knn = KNeighborsClassifier(n_neighbors=5)
    knn.fit(X_train, y_train)
    return knn

def train_decision_tree_model(df):
    features = ["size.1", "intelligence", "score for kids"]
    X = df[features]
    y = df["Breed"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    dt = DecisionTreeClassifier()
    dt.fit(X_train, y_train)
    return dt

def train_regression_models(df):
    models = {}
    target_columns = ["PURCHASE PRICE", "NUMBER OF GENETIC AILMENTS", "LONGEVITY(YEARS)"]
    features = ["size.1", "intelligence", "score for kids"]
    
    for target in target_columns:
        X = df[features]
        y = df[target]
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        model = LinearRegression()
        model.fit(X_train, y_train)
        models[target] = model
    
    return models

def main():
    st.title("반려견 정보 대시보드 🐶")
    st.write("이 앱은 다양한 개 품종의 정보를 제공합니다!")
    
    df, label_encoders = load_data()
    knn_model = train_knn_model(df)
    dt_model = train_decision_tree_model(df)
    reg_models = train_regression_models(df)
    
    st.header("🐾 반려견 추천 시스템")
    size_option = st.selectbox("크기 선택", label_encoders["size.1"].classes_)
    intelligence_option = st.selectbox("지능 수준", label_encoders["intelligence"].classes_)
    kids_score = st.slider("아이들과의 적합성 점수", 1.0, 5.0, 4.0)
    
    size_encoded = label_encoders["size.1"].transform([size_option])[0]
    intelligence_encoded = label_encoders["intelligence"].transform([intelligence_option])[0]
    user_input = [[size_encoded, intelligence_encoded, kids_score]]
    
    knn_prediction = knn_model.predict(user_input)[0]
    dt_prediction = dt_model.predict(user_input)[0]
    
    st.write(f"### 📌 KNN 추천 품종: {knn_prediction}")
    st.write(f"### 📌 Decision Tree 추천 품종: {dt_prediction}")
    
    st.header("💰 건강, 가격, 수명 예측")
    selected_breed = st.selectbox("예측할 품종 선택", df["Breed"].unique())
    breed_data = df[df["Breed"] == selected_breed][["size.1", "intelligence", "score for kids"]].values
    
    predicted_price = reg_models["PURCHASE PRICE"].predict(breed_data)[0]
    predicted_health = reg_models["NUMBER OF GENETIC AILMENTS"].predict(breed_data)[0]
    predicted_lifespan = reg_models["LONGEVITY(YEARS)"].predict(breed_data)[0]
    
    st.write(f"### 💲 예상 가격: ${predicted_price:,.2f}")
    st.write(f"### 🏥 예상 건강 문제 수: {predicted_health:.2f}개")
    st.write(f"### ⏳ 예상 수명: {predicted_lifespan:.1f}년")

if __name__ == "__main__":
    main()
