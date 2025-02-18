import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
import seaborn as sns



import os
import matplotlib.font_manager as fm

@st.cache_data
def fontRegistered():
    font_dirs = [os.getcwd() + '/custom_fonts']
    font_files = fm.findSystemFonts(fontpaths=font_dirs)
    for font_file in font_files:
        fm.fontManager.addfont(font_file)
    fm._load_fontmanager(try_read_cache=False)






def run_prediction():

    fontRegistered()
    plt.rc('font', family='NanumSquareNeo-bRg')

    df = pd.read_csv('dog/dog_breeds_data.csv')

    st.write(""" 
            ##### `[유형별 품종 수, 유형별 평균수명]`, `운동량과 평균 수명의 관계`, `지능과 훈련 난이도의 관계`,

            ##### `훈련이 쉬운 품종 TOP5`, `어린이와 친한 강아지 TOP5`
             
            위 데이터를 분석해서 차트로 표시했습니다.
            
            원하는 옵션을 선택해서 분석결과를 확인할 수 있습니다.
            
             """)
    
    st.divider()

    # 차트 선택
    st.subheader("📊 선택한 옵션에 따른 차트 보기")
    option = st.selectbox("분석할 항목을 선택하세요", ["유형별 품종 수, 유형별 평균수명", "운동량과 평균 수명의 관계", "지능과 훈련 난이도의 관계", "훈련이 쉬운 품종 TOP5", "어린이와 친한 강아지 TOP5"])
    if option == "유형별 품종 수, 유형별 평균수명":
        st.subheader("📌 유형별")
        st.info("""
            유형별 품종의 수와 수명을 분석합니다. 

            유형의 종류는 [토이, 하운드, 테리어, 워킹, 논-스포팅, 스포팅, 허딩, 스탠다드] 가 있습니다.    
                
            """)
        # 📌 강아지 유형별 설명 데이터 생성
        dog_types = {
            "유형": ["스포팅", "워킹", "하운드", "테리어", "토이", "논-스포팅", "허딩", "스탠다드"],
            "주요 특징": [
                "사냥 보조, 물놀이 좋아함", "경비, 구조, 썰매견", "사냥견, 뛰어난 후각과 속도",
                "설치류 사냥, 용감하고 활발", "작은 크기, 반려견 용도", "특정 작업 없이 다양한 목적",
                "가축 몰이, 영리하고 활동적", "반려견, 전시견"
            ],
            "대표 품종": [
                "리트리버, 스패니얼, 비즐라", "시베리안 허스키, 도베르만, 로트와일러", "바셋 하운드, 비글, 그레이하운드",
                "잭 러셀 테리어, 스코티시 테리어", "치와와, 말티즈, 포메라니안", "불독, 달마시안, 차우차우",
                "보더 콜리, 저먼 셰퍼드, 웰시 코기", "스탠다드 푸들, 불 테리어"
            ]
        }

        # 📌 데이터프레임 변환
        df_dog_types = pd.DataFrame(dog_types)

        # 📌 Streamlit에서 표 표시
        st.write("##### 📋 강아지 유형별 설명")
        st.table(df_dog_types)  # 표 표시
        
        col1, col2 = st.columns(2)
        
        with col1:
            type_counts = df["유형"].value_counts()
            custom_colors = sns.color_palette("pastel", len(type_counts))  # 🎨 박스플롯과 동일한 색상 적용

            data = df['유형'].value_counts()
            fig, ax = plt.subplots(figsize=(7, 4))
            ax.pie(data, labels=data.index, autopct="%1.1f%%", startangle=90, textprops={'fontsize':6}, colors=custom_colors)
            ax.set_title("유형별 품종 수")
            st.pyplot(fig)

        with col2:
            
            fig, ax = plt.subplots(figsize=(7, 4))
            sns.boxplot(x=df['유형'], y=df['수명 (년)'], ax=ax, palette='pastel')
            ax.set_title("유형별 수명", fontsize=16)
            ax.set_xlabel("유형", fontsize=12)
            ax.set_ylabel("수명(년)", fontsize=12)
            st.pyplot(fig)
        
    if option == "운동량과 평균 수명의 관계":
        st.subheader("📌 운동 필요량과 평균 수명의 관계")
        st.info("""
                강아지의 운동 필요량과 평균 수명 간의 관계를 분석합니다. 
                
                운동량이 많을수록 건강할 가능성이 높지만, 품종에 따라 차이가 있을 수 있습니다.
                """)
        # 운동 필요량별 평균 수명 계산
        exercise_lifespan = df.groupby("운동 필요량 (시간/일)")["수명 (년)"].mean()

        # 시각화
        fig, ax = plt.subplots(figsize=(7, 4))
        sns.lineplot(x=exercise_lifespan.index, y=exercise_lifespan.values, marker="o", ax=ax)
        ax.set_xlabel("운동 필요량 (시간/일)")
        ax.set_ylabel("평균 수명 (년)")
        ax.set_title("운동량과 평균 수명의 관계")
        st.pyplot(fig)  

    if option == "지능과 훈련 난이도의 관계":
        st.subheader("📌 지능과 훈련 난이도의 관계")
        st.info("""
                지능이 높은 강아지는 훈련이 쉬울 가능성이 높습니다. 

                이 차트는 강아지의 지능과 훈련 난이도 간의 관계를 보여줍니다.
                """)
        # 지능별 평균 훈련 난이도 계산
        intelligence_training = df.groupby("지능 (1-10)")["훈련 난이도 (1-10)"].mean()

        # 시각화
        fig, ax = plt.subplots(figsize=(9, 5))
        sns.scatterplot(x=intelligence_training.index, y=intelligence_training.values, ax=ax)
        ax.set_xlabel("지능")
        ax.set_ylabel("훈련 난이도")
        ax.set_title("지능과 훈련 난이도의 관계")
        st.pyplot(fig)



    if option == "훈련이 쉬운 품종 TOP5":
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

    if option == "어린이와 친한 강아지 TOP5":
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

