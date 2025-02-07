
import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
import time


def load_data():
    df = pd.read_csv('dog/dogs-ranking-dataset.csv')

    df2 = pd.read_csv('dog/dog_breeds.csv')

    df2_data = df2[ ['breed', 'url', 'img'] ]
    df2_data.rename(columns={'breed': '품종'}, inplace=True)

    df = df[df['품종'].isin(df2_data['품종'])].merge(df2_data,left_on='품종', right_on='품종', how='inner')

    breed_mapping = {
        "Border Terrier": "보더 테리어",
        "Cairn Terrier": "케언 테리어",
        "Siberian Husky": "시베리안 허스키",
        "Welsh Springer Spaniel": "웨일스 스프링거 스패니얼",
        "English Cocker Spaniel": "잉글리시 코커 스패니얼",
        "Cocker Spaniel": "코커 스패니얼",
        "Lhasa Apso": "라사 압소",
        "English Springer Spaniel": "잉글리시 스프링거 스패니얼",
        "Shetland Sheepdog": "셰틀랜드 쉽독 (셸티)",
        "West Highland White Terrier": "웨스트 하이랜드 화이트 테리어 (웨스티)",
        "Brittany": "브리타니 스패니얼",
        "German Shorthaired Pointer": "저먼 쇼트헤어드 포인터",
        "Pointer": "포인터",
        "Tibetan Spaniel": "티베탄 스패니얼",
        "Labrador Retriever": "래브라도 리트리버",
        "Bichon Frise": "비숑 프리제",
        "Irish Setter": "아이리시 세터",
        "Samoyed": "사모예드",
        "Shih Tzu": "시추",
        "Golden Retriever": "골든 리트리버",
        "Chesapeake Bay Retriever": "체서피크 베이 리트리버",
        "Papillon": "파피용",
        "Gordon Setter": "고든 세터",
        "English Setter": "잉글리시 세터",
        "Pug": "퍼그",
        "Affenpinscher": "아펜핀셔",
        "Miniature Schnauzer": "미니어처 슈나우저",
        "Beagle": "비글",
        "Border Collie": "보더 콜리",
        "Australian Terrier": "오스트레일리안 테리어",
        "Whippet": "휘핏",
        "Boston Terrier": "보스턴 테리어",
        "Briard": "브리아드",
        "Bedlington Terrier": "베들링턴 테리어",
        "Cavalier King Charles Spaniel": "카발리에 킹 찰스 스패니얼",
        "Dalmatian": "달마시안",
        "Flat-Coated Retriever": "플랫코티드 리트리버",
        "Belgian Tervuren": "벨지안 터뷰런",
        "Basset Hound": "바셋 하운드",
        "Poodle": "푸들",
        "Staffordshire Bull Terrier": "스태퍼드셔 불 테리어",
        "Bouvier des Flandres": "부비에 데 플랑드르",
        "Pembroke Welsh Corgi": "펨브록 웰시 코기",
        "Clumber Spaniel": "클럼버 스패니얼",
        "Pomeranian": "포메라니안",
        "Australian Shepherd": "오스트레일리안 셰퍼드",
        "Pharaoh Hound": "파라오 하운드",
        "Dandie Dinmont Terrier": "댄디 딘몬트 테리어",
        "Greyhound": "그레이하운드",
        "Saluki": "살루키",
        "Australian Cattle Dog": "오스트레일리안 캐틀독",
        "Tibetan Terrier": "티베탄 테리어",
        "Norfolk Terrier": "노퍽 테리어",
        "Dachshund": "닥스훈트",
        "Chihuahua": "치와와",
        "Doberman Pinscher": "도베르만 핀셔",
        "English Toy Spaniel": "잉글리시 토이 스패니얼",
        "Newfoundland": "뉴펀들랜드",
        "Basenji": "바센지",
        "Afghan Hound": "아프간 하운드",
        "Old English Sheepdog": "올드 잉글리시 쉽독",
        "French Bulldog": "프렌치 불독",
        "Bernese Mountain Dog": "버니즈 마운틴 독",
        "Boxer": "복서",
        "Brussels Griffon": "브뤼셀 그리펀",
        "Maltese": "몰티즈",
        "Giant Schnauzer": "자이언트 슈나우저",
        "Rottweiler": "로트와일러",
        "Yorkshire Terrier": "요크셔 테리어",
        "Irish Wolfhound": "아이리시 울프하운드",
        "Scottish Terrier": "스코티시 테리어",
        "Bullmastiff": "불마스티프",
        "German Shepherd": "저먼 셰퍼드",
        "Mastiff": "마스티프",
        "Great Dane": "그레이트 데인",
        "Kerry Blue Terrier": "케리 블루 테리어",
        "Italian Greyhound": "이탈리안 그레이하운드",
        "Pekingese": "페키니즈",
        "Rhodesian Ridgeback": "로디시안 리지백",
        "Bull Terrier": "불 테리어",
        "Saint Bernard": "세인트 버나드",
        "Borzoi": "보르조이",
        "Alaskan Malamute": "알래스칸 말라뮤트",
        "Bloodhound": "블러드하운드",
        "Chow Chow": "차우차우",
        "Akita": "아키타",
        "Bulldog": "불독"
    }
    df['품종'] = df['품종'].map(breed_mapping)


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
    
    st.subheader('강아지 품종을 추천해드립니다.')
    st.write("""
            <p style="color:#4B4B4B; font-size:17px; font-weight:400;">
    원하시는 개의 <b style="color:#FF8C00;">사이즈/지능/아이들과 적합성이 높은지 낮은지</b>를 선택하면
    </p>
    <p style="color:#4B4B4B; font-size:17px; font-weight:400;">
    그에 맞는 비슷한 품종을 찾아서 추천해드릴게요!
    </p>
    """, unsafe_allow_html=True)
    st.write('')
    
    
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

        st.write("### 📌 선택하신 조건으로 추천해드리는 품종입니다 :")
        for breed in top_2_breeds:
            st.write(f'- {breed}')
        
        for breed in top_2_breeds:
            breed_info = df.loc[df['품종'] == breed]

            if not breed_info.empty:
                breed_img = breed_info['img'].values[0]
                breed_url = breed_info['url'].values[0]
                
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