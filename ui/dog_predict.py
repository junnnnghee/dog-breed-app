from matplotlib import pyplot as plt
import matplotlib
import streamlit as st
import pandas as pd
import seaborn as sns

from sklearn.preprocessing import LabelEncoder, OrdinalEncoder
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


matplotlib.rc("font", family="Malgun Gothic")
matplotlib.rcParams["axes.unicode_minus"] = False


def run_prediction():
    df = pd.read_csv('dog/dog_breeds_data.csv')

    st.write("#### ")

    st.write("##### 📌 크기별 평균 수명")
    st.info("강아지 크기에 따라 평균 수명이 어떻게 다른지 보여줍니다. 보통 소형견이 대형견보다 오래 사는 경향이 있습니다.")
    # 크기별 평균 수명 계산
    size_lifespan = df.groupby("크기")["수명 (년)"].mean().sort_values()

    # 시각화
    fig, ax = plt.subplots(figsize=(9, 5))
    sns.barplot(x=size_lifespan.index, y=size_lifespan.values, ax=ax)
    ax.set_xlabel("강아지 크기")
    ax.set_ylabel("평균 수명 (년)")
    ax.set_title(" 크기별 평균 수명 비교")
    st.pyplot(fig)
     
    st.subheader("📌 운동 필요량과 평균 수명의 관계")
    st.info("강아지의 운동 필요량과 평균 수명 간의 관계를 분석합니다. 운동량이 많을수록 건강할 가능성이 높지만, 품종에 따라 차이가 있을 수 있습니다.")
    # 운동 필요량별 평균 수명 계산
    exercise_lifespan = df.groupby("운동 필요량 (시간/일)")["수명 (년)"].mean()

    # 시각화
    fig, ax = plt.subplots(figsize=(9, 5))
    sns.lineplot(x=exercise_lifespan.index, y=exercise_lifespan.values, marker="o", ax=ax)
    ax.set_xlabel("운동 필요량 (시간/일)")
    ax.set_ylabel("평균 수명 (년)")
    ax.set_title("운동량과 평균 수명의 관계")
    st.pyplot(fig)  

    st.subheader("📌 지능과 훈련 난이도의 관계")
    st.info("지능이 높은 강아지는 훈련이 쉬울 가능성이 높습니다. 이 차트는 강아지의 지능과 훈련 난이도 간의 관계를 보여줍니다.")
    # 지능별 평균 훈련 난이도 계산
    intelligence_training = df.groupby("지능 (1-10)")["훈련 난이도 (1-10)"].mean()

    # 시각화
    fig, ax = plt.subplots(figsize=(9, 5))
    sns.scatterplot(x=intelligence_training.index, y=intelligence_training.values, ax=ax)
    ax.set_xlabel("지능")
    ax.set_ylabel("훈련 난이도")
    ax.set_title("지능과 훈련 난이도의 관계")
    st.pyplot(fig)


    st.subheader("📌 훈련이 쉬운 품종 TOP 5")
    st.info("훈련 난이도가 낮은(쉽게 훈련 가능한) 강아지 품종을 보여줍니다. 초보 반려인에게 적합한 품종을 찾을 수 있습니다.")

    # 훈련 난이도가 낮은 품종 상위 5개 추출
    top_easy_train = df.nsmallest(5, "훈련 난이도 (1-10)")[["품종", "훈련 난이도 (1-10)"]]

    # 시각화
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.barplot(y=top_easy_train["품종"], x=top_easy_train["훈련 난이도 (1-10)"], ax=ax)
    ax.set_xlabel("훈련 난이도")
    ax.set_ylabel("품종")
    ax.set_title("훈련이 쉬운 품종 TOP 5")
    st.pyplot(fig)


    st.subheader("📌 어린이와 가장 친한 강아지 TOP 5")
    st.info("아이들과 잘 어울리는 강아지 품종을 보여줍니다. 어린이가 있는 가정에서 반려견을 선택할 때 유용한 정보입니다.")

    # 어린이 친화도가 높은 품종 상위 5개 추출
    top_kid_friendly = df[df["어린이 친화적 여부"] == "예"].nlargest(5, "친화도 (1-10)")[["품종", "친화도 (1-10)"]]

    # 시각화
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.barplot(y=top_kid_friendly["품종"], x=top_kid_friendly["친화도 (1-10)"], ax=ax)
    ax.set_xlabel("친화도")
    ax.set_ylabel("품종")
    ax.set_title("어린이와 가장 친한 강아지 TOP 5")
    st.pyplot(fig)

    