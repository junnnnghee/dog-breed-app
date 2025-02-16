
from sklearn.linear_model import LinearRegression
import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
import time
from sklearn.preprocessing import LabelEncoder



def load_data():
    df = pd.read_csv('dog/dog_breeds_data.csv')
    
        
    return df

    
df = load_data()



# 크기수치화 매핑
size_mapping = {
    "소형": [1, 1.5], 
    "중형": [1.5, 2], 
    "대형": [3]
}




    

def run_breed():
    
    st.subheader('강아지 품종을 추천해드립니다.')
    st.write("""
            <p style="color:#4B4B4B; font-size:17px; font-weight:400;">
    원하시는 개의 <b style="color:#FF8C00;">사이즈/지능/아이들과 적합성이 높은지 낮은지</b>를 선택하면
    </p>
    <p style="color:#4B4B4B; font-size:17px; font-weight:400;">
    그에 맞는 비슷한 품종을 찾아서 추천해드릴게요!
    </p>
    """, unsafe_allow_html=True)
    st.divider()
    st.write("""
        추천 품종 기능은 **KNN (K-Nearest Neighbors)** 알고리즘을 기반으로 구현되었습니다. 이 모델은 사용자가 입력한 **개의 크기**, **지능**, **아이들과의 적합성 점수**를 바탕으로 가장 적합한 품종을 추천합니다. 

        KNN 모델은 **주변의 유사한 품종**을 찾아, 사용자가 원하는 특성에 맞는 품종을 추천하는 방식입니다. 이 방법은 **직관적이고 효율적인 추천 시스템**으로, 다양한 특성에 맞는 품종을 빠르게 찾아줍니다.

        이 앱은 **데이터 기반**으로 작동하며, 사용자에게 최적의 반려견 품종을 찾는 데 도움을 줍니다.
        
        
        """)

    
    
    
           
    
    st.divider()
    
    st.write('###### 1️⃣ 기본 성향 관련')

    if 'category' not in st.session_state:
        st.session_state.category = False

    if st.button('추천 받기', key='first_bt'):
        st.session_state.category = not st.session_state.category

    if st.session_state.category:

        st.text('원하는 개의 사이즈, 지능, 아이들과의 적합성 점수를 선택하세요.')
        
        # 초기값을 '선택하세요'로 설정
        size_option = st.selectbox('사이즈', ["선택하세요"] + list(size_mapping.keys()))
        intelligence_option = st.number_input('지능 (4-10)', sorted(df['지능 (1-10)'].unique())[0],sorted(df['지능 (1-10)'].unique())[-1] )
        Affinity_option = st.number_input('친화도 (5-10)', sorted(df['친화도 (1-10)'].unique())[0],sorted(df['친화도 (1-10)'].unique())[-1])

        # 사용자가 3개 다 선택하지 않으면 예측하지 않음
        if size_option != "선택하세요" and intelligence_option != "선택하세요" and Affinity_option != "선택하세요":
            
            size_encoded = list(size_mapping.keys()).index(size_option) + 1
            
            user_input = [[size_encoded, intelligence_option, Affinity_option]]
            
            knn_model = train_knn_model(df, size_option)
            

            # 예측된 확률 가져오기
            knn_probabilities = knn_model.predict_proba(user_input)[0]

            # 확률이 높은 순으로 정렬하여 2개 추천
            sorted_indices = knn_probabilities.argsort()[::-1]  
            top_2_breeds = knn_model.classes_[sorted_indices[:2]]
            
            with st.spinner('loding...'):
                time.sleep(2)

            
            st.divider()
            

            st.write("### 📌 선택하신 조건으로 추천해드리는 품종입니다 :")
            for breed in top_2_breeds:
                st.write(f'- {breed}')
            
            
            for breed in top_2_breeds:
                breed_info = df.loc[df['품종'] == breed]

                if not breed_info.empty:
                    breed_img = breed_info['이미지'].values[0]
                    breed_url = breed_info['정보링크'].values[0]
                    
                    breed_size = breed_info['크기'].values[0]
                    if isinstance(breed_size, list):
                        breed_size = ", ".join(breed_size)  # 리스트면 문자열로 변환
                    else:
                        breed_size = str(breed_size).replace("[", "").replace("]", "").replace("'", "")
                    breed_intelligence = breed_info['지능 (1-10)'].values[0]
                    breed_Affinity = breed_info['친화도 (1-10)'].values[0]
                    breed_traits = breed_info['특징'].values[0]

                    

                    st.write(f"#### 🐶 {breed}")
                    # 개 품종 특징 출력
                    st.write(f"✅ **크기 :** {breed_size}")
                    st.write(f"✅ **지능 :** {breed_intelligence}")
                    st.write(f"✅ **친화도 :** {breed_Affinity}")
                    st.success(f"🏷️🐾 **특징 : {breed_traits}**")
                    st.image(breed_img, width=300)
                    st.write('##### 📌 자세한 정보를 알고 싶다면? 아래 링크를 클릭하세요❗')
                    st.page_link(breed_url, label='웹사이트 방문하기', icon="🌍")
                    st.divider()

                    

        else:
            st.warning("❗ 모든 옵션을 선택해야 추천이 나옵니다!")  # 선택이 안 된 경우 경고 메시지 출력

    st.divider()

    st.write('###### 2️⃣ 라이프스타일 관련 ')

    if 'category2' not in st.session_state:
        st.session_state.category2 = False

    if st.button('추천 받기',key='second_bt'):
        st.session_state.category2 = not st.session_state.category2

    if st.session_state.category2:
        exercise_mapping = {
            1: "1시간",
            1.5: "1.5시간",
            2: "2시간",
            2.5: "2.5시간",
            3: "3시간"
        }
        exercise_option = st.selectbox('운동시간', ['선택하세요']+ list(exercise_mapping.values()))
        child_option = st.radio('어린이 친화적 여부', list(df['어린이 친화적 여부'].unique()))
        training_option = st.number_input('훈련 난이도(4-10)', sorted(df['훈련 난이도 (1-10)'].unique())[0],sorted(df['훈련 난이도 (1-10)'].unique())[-1])

        if exercise_option != "선택하세요" and child_option != "선택하세요" and training_option != "선택하세요":
            exercise_numeric = list(exercise_mapping.keys())[list(exercise_mapping.values()).index(exercise_option)]
        
            knn_model2, label_encoder = train_knn_model2(df)
            child_numeric = label_encoder.transform([child_option])[0]
            user_input = [[exercise_numeric, child_numeric, training_option]]

            # 예측된 확률 가져오기
            knn_probabilities = knn_model2.predict_proba(user_input)[0]

            # 확률이 높은 순으로 정렬하여 2개 추천
            sorted_indices = knn_probabilities.argsort()[::-1]  
            top_2_breeds = knn_model2.classes_[sorted_indices[:2]]
            
            with st.spinner('loding...'):
                time.sleep(2)

            
            st.divider()
            

            st.write("### 📌 선택하신 조건으로 추천해드리는 품종입니다 :")
            for breed in top_2_breeds:
                st.write(f'- {breed}')
            
            
            for breed in top_2_breeds:
                breed_info = df.loc[df['품종'] == breed]

                if not breed_info.empty:
                    breed_img = breed_info['이미지'].values[0]
                    breed_url = breed_info['정보링크'].values[0]
                    
                    
                    breed_exercise_numeric = breed_info['운동 필요량 (시간/일)'].values[0]
                    breed_exercise = exercise_mapping.get(breed_exercise_numeric, f"{breed_exercise_numeric}시간")
                    breed_child = breed_info['어린이 친화적 여부'].values[0]
                    breed_training = breed_info['훈련 난이도 (1-10)'].values[0]
                    breed_traits = breed_info['특징'].values[0]
                    
                    
                    st.write(f"#### 🐶 {breed}")
                    # 개 품종 특징 출력
                    st.write(f"✅ **운동 필요한 시간 :** {breed_exercise}")
                    st.write(f"✅ **어린이 친화적 여부 :** {breed_child}")
                    st.write(f"✅ **훈련 난이도 :** {breed_training}")
                    st.success(f"🏷️🐾 **특징 : {breed_traits}**")
                    st.image(breed_img, width=300)
                    st.write('##### 📌 자세한 정보를 알고 싶다면? 아래 링크를 클릭하세요❗')
                    st.page_link(breed_url, label='웹사이트 방문하기', icon="🌍")
                    st.divider()

                    

        else:
            st.warning("❗ 모든 옵션을 선택해야 추천이 나옵니다!")  # 선택이 안 된 경우 경고 메시지 출력
    
    st.divider()
    
    st.write('###### 3️⃣ 반려견 관리 관련 ')

    if 'category3' not in st.session_state:
        st.session_state.category3 = False

    if st.button('추천 받기',key='third_bt'):
        st.session_state.category3 = not st.session_state.category3

    if st.session_state.category3:
        custom_order = ["낮음", "보통", "높음", "매우 높음"]

        grooming_option = st.selectbox('손질필요도', ['선택하세요']+ sorted(df["손질 필요도"].unique(), key=lambda x: custom_order.index(x)))
        shedding_option = st.selectbox('털 빠짐 정도', ['선택하세요']+ sorted(df["털 빠짐 정도"].unique(), key=lambda x: custom_order.index(x)))
        health_option = st.selectbox('건강 문제 위험', ['선택하세요']+ sorted(df["건강 문제 위험"].unique(), key=lambda x: custom_order.index(x)))

        if grooming_option != '선택하세요' and shedding_option != '선택하세요' and health_option != '선택하세요':
            
            knn_model3, encoders = train_knn_model3(df)

            grooming_encoded= encoders['손질 필요도'].transform([grooming_option])[0]
            shedding_encoded = encoders['털 빠짐 정도'].transform([shedding_option])[0]
            health_encoded = encoders['건강 문제 위험'].transform([health_option])[0]

            user_input = [[grooming_encoded, shedding_encoded, health_encoded]]

            # 예측된 확률 가져오기
            knn_probabilities = knn_model3.predict_proba(user_input)[0]

            # 확률이 높은 순으로 정렬하여 2개 추천
            sorted_indices = knn_probabilities.argsort()[::-1]  
            top_2_breeds = knn_model3.classes_[sorted_indices[:2]]
            
            with st.spinner('loding...'):
                time.sleep(2)

            
            st.divider()
            

            st.write("### 📌 선택하신 조건으로 추천해드리는 품종입니다 :")
            for breed in top_2_breeds:
                st.write(f'- {breed}')
                
            
            for breed in top_2_breeds:
                breed_info = df.loc[df['품종'] == breed]

                if not breed_info.empty:
                    breed_img = breed_info['이미지'].values[0]
                    breed_url = breed_info['정보링크'].values[0]
                    
                    
                    breed_grooming = breed_info['손질 필요도'].values[0]
                    breed_shedding = breed_info['털 빠짐 정도'].values[0]
                    breed_health = breed_info['건강 문제 위험'].values[0]
                    breed_traits = breed_info['특징'].values[0]

                    
                    st.write(f"#### 🐶 {breed}")
                    # 개 품종 특징 출력
                    st.write(f"✅ **손질 필요도 :** {breed_grooming}")
                    st.write(f"✅ **털 빠짐 정도 :** {breed_shedding}")
                    st.write(f"✅ **건강 문제 위험 :** {breed_health}")
                    st.success(f"🏷️🐾 **특징 : {breed_traits}**")
                    st.image(breed_img, width=300)
                    st.write('##### 📌 자세한 정보를 알고 싶다면? 아래 링크를 클릭하세요❗')
                    st.page_link(breed_url, label='웹사이트 방문하기', icon="🌍")
                    similar_breeds = knn_model3.classes_[sorted_indices[:5]]  # 상위 5개 추천

                    st.divider()

                    

        else:
            st.warning("❗ 모든 옵션을 선택해야 추천이 나옵니다!")  # 선택이 안 된 경우 경고 메시지 출력
    










def train_knn_model(df, selected_size):
    # 크기 수치화 매핑 (사용자가 선택한 크기에 따라 범위 설정)
    size_mapping = {
        "소형": [1, 1.5], 
        "중형": [1.5, 2], 
        "대형": [3]
    }

    selected_size_range = size_mapping[selected_size] # 사용자가 선택한 크기 범위

    # 사용자가 선택한 크기 수치화 값과 일치하는 데이터만 필터링
    df_filtered = df[df["크기 수치화"].isin(selected_size_range)]
        
    y = df_filtered['품종']
    X = df_filtered[['크기 수치화', '지능 (1-10)', '친화도 (1-10)']]

    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    knn = KNeighborsClassifier(n_neighbors=2)
    knn.fit(X_train, y_train)
    
    return knn

def train_knn_model2(df):
       
    
        
    y = df['품종']
    X = df[['운동 필요량 (시간/일)','어린이 친화적 여부', '훈련 난이도 (1-10)']]

    label_encoder = LabelEncoder()
    X['어린이 친화적 여부'] = label_encoder.fit_transform(X['어린이 친화적 여부'])
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    knn2 = KNeighborsClassifier(n_neighbors=2)
    knn2.fit(X_train, y_train)
    
    return knn2, label_encoder


def train_knn_model3(df):
       
    y = df['품종']
    X = df[['손질 필요도', '털 빠짐 정도','건강 문제 위험']]

    encoders = {}  # 각 컬럼별 LabelEncoder 저장
    for col in X.columns:
        le = LabelEncoder()
        X[col] = le.fit_transform(X[col])  # 각 컬럼 변환
        encoders[col] = le  # 변환된 LabelEncoder 저장 (예측 시 사용)
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    knn3 = KNeighborsClassifier(n_neighbors=2)
    knn3.fit(X_train, y_train)
    
    return knn3, encoders