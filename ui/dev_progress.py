import pandas as pd
import streamlit as st


def run_dev_progress():

    st.markdown("""
    이 앱은 **Streamlit을 활용하여 개발**되었으며,
                
    🔖추천 품종 기능은 **KNN (K-Nearest Neighbors)** 알고리즘을 기반으로 구현되었습니다.

    KNN 모델은 **주변의 유사한 품종**을 찾아, 사용자가 원하는 특성에 맞는 품종을 추천하는 방식입니다. 이 방법은 **직관적이고 효율적인 추천 시스템**으로, 다양한 특성에 맞는 품종을 빠르게 찾아줍니다.

    이 앱은 **데이터 기반**으로 작동하며, 사용자에게 최적의 반려견 품종을 찾는 데 도움을 줍니다.
                
    

    ---

    ## ✅ 개발 단계
    #### 1️⃣ **데이터 수집 및 전처리**  
        📥 CSV 파일 기반 데이터 정리
                  
    #### 2️⃣ **머신러닝 모델 개발**  
        🔎 KNN 기반 추천 시스템 구축  
     
    #### 3️⃣ **Streamlit UI 구축**  
        🖥️ 강아지 추천 & 데이터 분석을 위한 대시보드 설계 
                 
    #### 4️⃣ **추가 기능 개선**  
        🖼️ 이미지 업로드로 품종 판별 (예정)

    ---

    ## 🛠️ 데이터 수집 & 전처리
    📥 **CSV 데이터 수집**: 
    1. 캐글 데이터셋에 강아지 159개의 품종데이터를 확보 `Dog Breed Around The World.csv`
    2. 캐글 데이터셋에 강아지 563개에 대한 품종 정보와 이미지,링크 주소가 포함된 데이터를 확보 `dog_breeds.csv`
    
    🔍 **데이터 정리**:
    - `Dog Breed Around The World.csv` 데이터의 품종을 기준으로 `dog_breeds.csv` 데이터와 결합
    - `dog_breeds.csv` 에서 이미지, 링크를 제외한 컬럼 삭제
    - 영어로 되어있는 데이터를 한글로 변환
    - 레이블 인코딩하여 학습 (ex: `건강 문제 위험` → 숫자로 변환)
    - 크기 수치화 컬럼 추가
        > Small, Medium, Large, Giant, Small-Medium, Small_Large
        
        > Giant는 대형에도 속하기 때문에 대형으로 변경했습니다.
        
        > 같은 품종이여도 두개의 크기로 나뉘어지는 품종들도 있습니다.
        
        > 수정한 데이터에는 사용자가 보기 쉽게[소형, 중형] 리스트 형식으로 변경했고
        
        > 크기 수치화 컬럼을 추가했습니다. -> `1, 1.5, 2, 3`
    """)
    
    # 📌 기존 데이터셋 (Kaggle 원본)
    df_original = pd.read_csv("dog/Dog Breads Around The World.csv")

    # 📌 수정된 데이터셋
    df_modified = pd.read_csv("dog/dog_breeds_data.csv")

    st.subheader("📊 데이터셋 비교")

    # 📌 컬럼명 비교
    st.write("##### 📌 1️⃣ 기존데이터와 수정된 데이터셋 비교")
    col1, col2 = st.columns(2)
    with col1:
        st.write("🗂 **기존 데이터셋 (Kaggle)**")
        st.dataframe(df_original)

    with col2:
        st.write("📝 **수정된 데이터셋**")
        st.dataframe(df_modified)

    st.write("")
    st.error("""
             ### 추가적인 문제 해결 과정
             
             품종 이름이 다르거나, 언어가 달라서 특정 품종이 결합이 안된 문제가 있었습니다.

             추가로 품종이 없는 것도 있어서 따로 추가했습니다.
             """)
    st.markdown("""
                #### `dog_breeds.csv` 데이터
                - ##### 1. 중복값이 있었음
                
                    > Affenpinscher, Ca Mè Mallorquí, Old Croatian Sighthound 컬럼 제거
                    
                - ##### 2. 품종 이름이 영어가 아닌 다른언어가 있어서 결합이 안되는 문제 발생

                    > Bichon Frisé -> Bichon Frise
                    
                    > Löwchen -> Lowchen
                
                    > Petit Basset Griffon Vendéen -> Petit Basset Griffon Vendeen
                
                - ##### 3. 품종은 같으나, 기준데이터 `Dog Breed Around The World.csv`와 이름이 다르게 기입되어 있음

                    > American Eskimo Dog -> American Eskimo
                    
                    > Chinese Crested Dog -> Chinese Crested
                    
                    > Shar Pei -> Chinese Shar-Pei
                    
                    > Dobermann -> Doberman Pinscher
                    
                    > Bulldog -> English Bulldog
                
                - ##### 4. 이미지, 정보를 가져오려고 하는데 없는 품종이 있음

                    > Poodle (Miniature), Poodle (Standard), Poodle (Toy), Great Pyrenees, English Toy Spaniel, Xoloitzcuintli
                
                    > 위 품종을 직접 검색해서 링크주소와, 이미지 링크 주소를 가져와서

                    > 데이터프레임으로 만든 뒤 기존 데이터에 추가함
                
                    > ###### Xoloitzcuintli는 Xoloitzcuintle로 데이터가 있었지만 품종이름이 다르게 되어있어서 따로 추가함

                #### `Dog Breed Around The World.csv` 데이터

                - ##### 1. 품종 이름 변경
                    > Cocker Spaniel -> American Cocker Spaniel
                
                    > Collie -> Rough Collie
                
                    > Mastiff > English Mastiff

                - ##### 2. 평균 체중의 값이 25-Jul 로 잘못 표기되어있음
                    > 25-Jul은 25~7kg 범위를 의미함
                
                    > 평균값으로 수동으로 데이터 변환 -> 16
                """)
    # 📌 데이터 수정 내용 정리
    modifications_dog_breeds = {
        "수정 내용": [
            "중복값 제거 (Affenpinscher, Ca Mè Mallorquí, Old Croatian Sighthound)",
            "품종명 영어 통일 (Bichon Frisé → Bichon Frise, Löwchen → Lowchen)",
            "기준 데이터와 품종명 통일 (American Eskimo Dog → American Eskimo, Bulldog → English Bulldog 등)",
            "누락된 이미지 및 정보 추가 (Poodle (Miniature), Great Pyrenees 등)",
            "품종명이 달라서 결합이 안 되는 문제 해결 (Xoloitzcuintli → Xoloitzcuintle)"
        ]
    }

    modifications_dog_around_world = {
        "수정 내용": [
            "품종명 변경 (Cocker Spaniel → American Cocker Spaniel, Mastiff → English Mastiff)",
            "평균 체중 값 오류 수정 (25-Jul → 25~7kg → 평균값으로 변환)"
        ]
    }

    # 📌 데이터프레임 변환
    df_breeds = pd.DataFrame(modifications_dog_breeds)
    df_around_world = pd.DataFrame(modifications_dog_around_world)

    # 📌 Streamlit에서 표 표시
    st.subheader("📋 dog_breeds.csv 데이터 수정 사항")
    st.table(df_breeds)

    st.subheader("📋 Dog Breed Around The World.csv 데이터 수정 사항")
    st.table(df_around_world)


    st.markdown("""
    ---

    ## 🧑‍💻 모델 개발 및 예측결과 평가
    - 🔎 **KNN 모델 활용**: 사용자의 성향에 맞는 강아지를 추천 
    - ⚖️ **예측결과 평가**: 사용자의 입력 기반으로 예측이 잘되는지 항목별 옵션을 선택해 직접 확인함  
    - 📊 **데이터 시각화**: 분석 결과를 차트와 그래프로 제공

    ---

    ## 🚀 배포 과정  
    - 이 앱은 **Streamlit Community Cloud**를 활용하여 배포되었습니다.  
    배포 과정에서 **requirements.txt** 파일을 생성하여 패키지를 관리하고, GitHub에 업로드한 후 배포를 진행하였습니다. 
                
    ---
    
    ## 📌 데이터셋 출처/품종 정보 출처
    데이터셋(캐글)
                
    https://www.kaggle.com/
    > [dog_breeds.csv](https://www.kaggle.com/datasets/edoardoba/dog-breeds)
                
    > [Dog Breeds Around The World.csv](https://www.kaggle.com/datasets/prajwaldongre/top-dog-breeds-around-the-world)
                
    직접 추가한 품종 링크, 이미지의 출처
                
    > https://www.akc.org/

    ---                    
    ## 📌 내 깃허브 주소
    [github.com/dog-breed-app](https://github.com/junnnnghee/dog-breed-app)
                

                
                
                
    
    
    """)


    