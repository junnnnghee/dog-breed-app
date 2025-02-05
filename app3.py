import streamlit as st
import pandas as pd

# 데이터 로드


def main():
    st.title("반려견 정보 대시보드 🐶")
    st.write("이 앱은 다양한 개 품종의 정보를 제공합니다!")

    df = pd.read_csv('dog/dogs-ranking-dataset.csv')
    
    st.dataframe(df.head())  # 데이터 미리보기
    
    # 반려견 선택 가이드
    st.header("🐾 반려견 선택 가이드")
    size_option = st.selectbox("크기 선택", ["All", "small", "medium", "large"])
    intelligence_option = st.selectbox("지능 수준", ["All", "Average", "Above average", "Excellent"])
    kids_option = st.selectbox("아이들과의 적합성", ["All", "High (4.5+)", "Medium (4.0-4.5)", "Low (<4.0)"])
    
    filtered_df = df.copy()
    if size_option != "All":
        filtered_df = filtered_df[filtered_df["size.1"] == size_option]
    if intelligence_option != "All":
        filtered_df = filtered_df[filtered_df["intelligence"] == intelligence_option]
    if kids_option == "High (4.5+)":
        filtered_df = filtered_df[filtered_df["score for kids"] >= 4.5]
    elif kids_option == "Medium (4.0-4.5)":
        filtered_df = filtered_df[(filtered_df["score for kids"] >= 4.0) & (filtered_df["score for kids"] < 4.5)]
    elif kids_option == "Low (<4.0)":
        filtered_df = filtered_df[filtered_df["score for kids"] < 4.0]
    
    st.write(f"### 🔍 추천 품종 ({len(filtered_df)}종)")
    st.dataframe(filtered_df[["Breed", "size.1", "intelligence", "score for kids"]])

    # 필터링 기능 추가 예정
    # 비교 도구 추가 예정
    # 비용 계산기 추가 예정
    # 순위 대시보드 추가 예정
    # 건강 분석 추가 예정

if __name__ == "__main__":
    main()
