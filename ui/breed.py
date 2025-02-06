
import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
import time


def load_data():
    df = pd.read_csv('dog/dogs-ranking-dataset.csv')

    

    # 크기를 수동으로 매핑 (문자열 → 숫자 변환)
    size_levels = {
        "small": 0,
        "medium": 1,
        "large": 2
    }
    df['크기'] = df['크기'].map(size_levels)
    
    
    
    # 지능 수준을 수동으로 매핑 (문자열 → 숫자 변환)
    intelligence_levels = {
        "Lowest": 0,  # 최하
        "Fair": 1,       # 낮음
        "Average": 2,   # 평균
        "Above average": 3,      # 평균 이상
        "Brightest": 4,  # 뛰어남
        "Excellent": 5 # 최고
    }
    df["지능"] = df["지능"].map(intelligence_levels)

    df2 = pd.read_csv('dog/dog_breeds.csv')

    df2_data = df2[ ['breed', 'url', 'img'] ]
    df2_data.rename(columns={'breed': '품종'}, inplace=True)

    df = df[df['품종'].isin(df2_data['품종'])].merge(df2_data,left_on='품종', right_on='품종', how='inner')
        
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
    st.write('###### 💡 인기순위 Top5 정보가 궁금하다면? 아래버튼 클릭 ❗')

    
    if 'show_top5' not in st.session_state:
        st.session_state.show_top5 = False

    
    if st.button('인기순위 Top5') :
        st.session_state.show_top5 = not st.session_state.show_top5
        
    if st.session_state.show_top5:
        st.text('🔻 아래는 개 품종 인기순위 Top5 정보입니다.')
        st.dataframe(df.sort_values('인기순위', ascending=True).head())
           
    

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
        knn_prediction = knn_model.predict(user_input)[0]  # 단 하나의 예측 결과만 가져오기
        
        with st.spinner('loding...'):
            time.sleep(2)

        st.write("### 📌 선택하신 조건으로 추천해드리는 품종입니다 :")
        st.write(f"- {knn_prediction}")  # 예측된 품종 하나만 출력
        
        breed_info = df.loc[df['품종'] == knn_prediction]
        breed_img = breed_info['img'].values[0]
        st.image(breed_img)
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