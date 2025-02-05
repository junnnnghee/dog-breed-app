import streamlit as st
import pandas as pd
from sklearn.cluster import KMeans
import numpy as np

# 📌 샘플 강아지 데이터
data = pd.DataFrame({
    "강아지_ID": [1, 2, 3, 4, 5],
    "나이": [2, 5, 3, 1, 4],
    "크기": [1, 2, 1, 0, 2],  # 소형(0), 중형(1), 대형(2)
    "사회성": [8, 6, 9, 7, 5],
    "활동성": [9, 5, 8, 6, 7],
    "공격성": [2, 3, 1, 4, 3],
    "분리불안": [5, 6, 3, 7, 4],
    "장난기": [7, 4, 9, 8, 6]
})

# K-Means 클러스터링 적용
features = data[["사회성", "활동성", "공격성", "분리불안", "장난기"]]
kmeans = KMeans(n_clusters=3, random_state=42)  # 3개의 그룹으로 클러스터링
data["그룹"] = kmeans.fit_predict(features)

# 📌 스트림릿 UI
st.title("🐶 강아지 사회성 매칭 추천")
st.sidebar.header("강아지 선택")
selected_id = st.sidebar.selectbox("강아지를 선택하세요", data["강아지_ID"])

if st.button("비슷한 강아지 추천"):
    group = data.loc[data["강아지_ID"] == selected_id, "그룹"].values[0]
    matched_dogs = data[data["그룹"] == group]
    st.write("📌 비슷한 사회성을 가진 강아지들:")
    st.write(matched_dogs[["강아지_ID", "사회성", "활동성", "장난기"]])
