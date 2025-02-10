
from sklearn.linear_model import LinearRegression
import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
import time


def load_data():
    df = pd.read_csv('dog_data.csv')
    
        
    return df

    
df = load_data()



# 크기를 사용자 친화적인 이름으로 매핑
size_mapping = {
    0: "small",
    1: "medium",
    2: "large"
}

# 지능 수준을 사용자 친화적인 이름으로 매핑
intelligence_mapping = {
    0: "최저",
    1: "낮음",
    2: "평균",
    3: "평균 이상",
    4: "뛰어남",
    5: "최고"
}
# 아이들과의 적합성 점수를 사용자 친화적인 이름으로 매핑
kids_mapping = {
    1: "높은 적합성",
    2: "중간 적합성",
    3: "낮은 적합성"
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
    st.write('###### 💡 인기순위 Top5가 궁금하다면? 아래버튼 클릭 ❗')


    
    if 'show_top5' not in st.session_state:
        st.session_state.show_top5 = False

    
    if st.button('인기순위 Top5') :
        st.session_state.show_top5 = not st.session_state.show_top5
        
    if st.session_state.show_top5:
        st.text('🔻 아래는 개 품종 인기순위 Top5 입니다.')
        dog_top5 = df.loc[:,['품종', '점수', '인기순위', '어린이를 위한 점수', '지능%']].sort_values('인기순위', ascending=True).reset_index(drop=True).head()
        dog_top5.index = range(1, len(dog_top5)+1)
        st.dataframe(dog_top5)
           
    
    st.divider()

    st.text('원하는 개의 사이즈, 지능, 아이들과의 적합성 점수를 선택하세요.')
    
    # 초기값을 '선택하세요'로 설정
    size_option = st.selectbox('사이즈', ["선택하세요"] + list(size_mapping.values()))
    intelligence_option = st.selectbox('지능 수준', ["선택하세요"] + list(intelligence_mapping.values()))
    kids_option = st.selectbox('어린이 적합성', ["선택하세요"] + list(kids_mapping.values()))

    # 사용자가 3개 다 선택하지 않으면 예측하지 않음
    if size_option != "선택하세요" and intelligence_option != "선택하세요" and kids_option != "선택하세요":
        size_encoded = list(size_mapping.keys())[list(size_mapping.values()).index(size_option)]
        intelligence_encoded = list(intelligence_mapping.keys())[list(intelligence_mapping.values()).index(intelligence_option)]
        kids_encoded = list(kids_mapping.keys())[list(kids_mapping.values()).index(kids_option)]
        
        user_input = [[size_encoded, intelligence_encoded, kids_encoded]]
        
        knn_model = train_knn_model(df)
        

        # 예측된 확률 가져오기
        knn_probabilities = knn_model.predict_proba(user_input)[0]

        # 확률이 높은 순으로 정렬하여 2개 추천
        sorted_indices = knn_probabilities.argsort()[::-1]  
        top_2_breeds = knn_model.classes_[sorted_indices[:2]]
        
        with st.spinner('loding...'):
            time.sleep(2)

        
        st.divider()
        
        
        st.write("### 📌 선택하신 조건으로 추천해드리는 품종입니다 :")
        st.warning('선택하신 조건의 3개가 ')
        for breed in top_2_breeds:
            st.write(f'- {breed}')
        
        
        for breed in top_2_breeds:
            breed_info = df.loc[df['품종'] == breed]

            if not breed_info.empty:
                breed_img = breed_info['이미지'].values[0]
                breed_url = breed_info['정보링크'].values[0]
                
                breed_size = breed_info['크기'].values[0]
                breed_intelligence = breed_info['지능'].values[0]
                breed_kids_friendly = breed_info['어린이 적합성'].values[0]

                # 숫자를 다시 사용자 친화적인 값으로 변환
                breed_size = size_mapping[breed_size]
                breed_intelligence = intelligence_mapping[breed_intelligence]
                breed_kids_friendly = kids_mapping[breed_kids_friendly]

                st.write(f"#### 🐶 {breed}")
                # 개 품종 특징 출력
                st.write(f"✅ **크기:** {breed_size}")
                st.write(f"✅ **지능:** {breed_intelligence}")
                st.write(f"✅ **어린이 적합성:** {breed_kids_friendly}")
                st.image(breed_img, width=300)
                st.write('##### 📌 자세한 정보를 알고 싶다면? 아래 링크를 클릭하세요❗')
                st.page_link(breed_url, label='웹사이트 방문하기', icon="🌍")
                st.divider()

                

    else:
        st.warning("❗ 모든 옵션을 선택해야 추천이 나옵니다!")  # 선택이 안 된 경우 경고 메시지 출력

    
    
    

def train_knn_model(df):
        
    y = df['품종']
    X = df.loc[ : , ['크기', '지능', '어린이 적합성'] ]

    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    knn = KNeighborsClassifier(n_neighbors=2)
    knn.fit(X_train, y_train)
    
    return knn


def train_decision_tree_model(df):

    y = df['품종']
    X = df.loc[ : , ['크기', '지능', '어린이 적합성'] ]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    dt = DecisionTreeClassifier()
    dt.fit(X_train, y_train)
    return dt