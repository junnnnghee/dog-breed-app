
import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier


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
    st.subheader('품종을 추천해드립니다.')


    st.text('아래는 개 품종 순위 Top5 정보입니다.')
    st.dataframe(df.head())       
    

    st.text('원하는 개의 사이즈, 지능, 아이들과의 적합성 점수를 선택하세요.')
    
    size_labels = [size_mapping[i] for i in range(len(size_mapping))]
    size_option = st.selectbox('사이즈', size_labels)
    size_encoded = list(size_mapping.keys())[size_labels.index(size_option)]

    st.text('지능')
    intelligence_labels = [intelligence_mapping[i] 
     for i in range(len(intelligence_mapping))]
    intelligence_option = st.selectbox('지능 수준', intelligence_labels)
    intelligence_encoded = list(intelligence_mapping.keys())[intelligence_labels.index(intelligence_option)]

    
    kisd_option = st.selectbox('어린이 적합성을 선택하세요.', list(kids_mapping.values()))
    kids_encoded = list(kids_mapping.keys())[list(kids_mapping.values()).index(kisd_option)]

    user_input = [ [size_encoded, intelligence_encoded, kids_encoded] ]

    knn_model = train_knn_model(df)
    dt_model = train_decision_tree_model(df)

   

    knn_probabilities = knn_model.predict_proba(user_input)[0]  # 품종별 확률 가져오기
    top_2_indices = knn_probabilities.argsort()[-2:][::-1]  # 확률이 높은 3개 품종 인덱스
    top_2_breeds = knn_model.classes_[top_2_indices]  # 인덱스에 해당하는 품종 가져오기

    st.write(f'사이즈 : {size_option}')
    st.write(f'지능 : {intelligence_option}')
    st.write(f'어린이 적합성 : {kisd_option}')

    st.write("### 📌 KNN 추천 품종:")
    for breed in top_2_breeds:
        st.write(f"- {breed}")
    
    
    

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