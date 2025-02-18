# 🐶 Dog Breed Recommendation & Analysis App

**Dog breed App** 은 강아지 품종 추천 기능과 데이터 분석 차트를 제공하는 Streamlit 기반 웹 애플리케이션입니다.

### 📌 [🔗 바로가기: Dog Breed App](https://dog-breed-app-uutmb4jpkftojqtu3dbkfm.streamlit.app/)  

## 📢 소개  
이 프로젝트는 Streamlit을 활용하여 **강아지 품종 추천 및 데이터 분석**을 제공하는 웹 애플리케이션입니다.  
사용자는 자신의 라이프스타일 및 선호도를 입력하여 **최적의 강아지 품종을 추천**받을 수 있으며, 다양한 **데이터 분석 차트**를 통해 강아지 품종별 특징을 확인할 수 있습니다.  

---

## 🎯 주요 기능
✅ **🐕 강아지 품종 추천**  
- 사용자의 선택(크기, 지능, 친화도 등)에 따라 **KNN 모델 기반 추천**  
- 라이프스타일(운동량, 훈련 난이도 등)에 따라 맞춤 품종 추천
- 반려견 관리 관련(손질 필요도, 털빠짐 정도, 건강문제 위험)에 따라 맞춤 품종 추천

✅ **📊 데이터 분석**  
- 강아지 **유형별 분포 및 평균 수명 분석**  
- **운동량과 평균 수명의 관계** 시각화  
- **지능과 훈련 난이도 관계 분석**  
- **어린이 친화적인 품종 TOP 5**  

✅ **🔍 품종 검색 기능**  
- 원하는 품종을 선택하면 **해당 품종의 상세 정보**를 볼 수 있음 

---

## 📊 데이터 분석 개요  

### 📌 **1️⃣ 유형별 품종 비율**
> 강아지 품종은 [토이, 하운드, 테리어, 워킹, 논-스포팅, 스포팅, 허딩, 스탠다드] 8가지로 구분됩니다.  
> **각 유형별 품종 수 및 평균 수명 차트를 제공하여 특징을 쉽게 확인할 수 있습니다.**


### 📌 **2️⃣ 운동 필요량과 평균 수명의 관계**
> 운동량이 많은 품종이 평균적으로 더 오래 사는가?  
> **운동 필요량과 평균 수명 간의 관계를 분석한 그래프 제공**


### 📌 **3️⃣ 지능과 훈련 난이도의 관계**
> 지능이 높은 강아지는 훈련이 쉬운가?  
> **지능 점수와 훈련 난이도 간의 관계를 분석한 차트 제공**  

---

## 🧑‍💻 사용된 기술  

✅ **프로그래밍 언어:** Python  
✅ **웹 프레임워크:** Streamlit  
✅ **머신러닝 모델:** KNN (품종 추천)    
✅ **데이터 분석 & 시각화:** Pandas, Matplotlib, Seaborn  
✅ **배포:** Streamlit Community Cloud

---

## 🚀 실행 방법
### 설치 & 환경 설정
먼저, 필요한 라이브러리를 설치해야 합니다.  
아래 명령어를 실행하여 패키지를 설치하세요. 

```bash
pip install -r requirements.txt

# 애플리케이션 실행
streamlit run app.py
```

---
## 🚀 개발 과정
이 프로젝트는 캐글에 데이터셋을 활용하여 다양한 강아지 품종 데이터를 기반으로 하며
두개의 csv 파일을 결합하여 수정 및 정제되었습니다.

📌 데이터 수집:
- Keggle 데이터셋에 강아지 159개의 품종데이터를 확보
- Keggle 데이터셋에 강아지 563개에 대한 품종 정보와 이미지,링크 주소가 포함된 데이터를 확보
- 이미지, 품종 정보가 없는 강아지를 직접 수집

📌 데이터 전처리 과정:

- Dog Breed Around The World.csv 데이터의 품종을 기준으로 dog_breeds.csv 데이터와 결합

- dog_breeds.csv 에서 이미지, 링크를 제외한 컬럼 삭제

- 영어로 되어있는 데이터를 한글로 변환

- 레이블 인코딩하여 학습 (ex: 건강 문제 위험 → 숫자로 변환)

- 크기 수치화 컬럼 추가

  > Small, Medium, Large, Giant, Small-Medium, Small_Large

  > Giant는 대형에도 속하기 때문에 대형으로 변경했습니다.

  > 같은 품종이여도 두개의 크기로 나뉘어지는 품종들도 있습니다.

  > 수정한 데이터에는 사용자가 보기 쉽게[소형, 중형] 리스트 형식으로 변경했고

  > 크기 수치화 컬럼을 추가했습니다. → `1, 1.5, 2, 3`

  
### 📌 추가 문제 해결 과정:
#### `dog_breeds.csv` 데이터
- ##### 1. 중복값이 있었음

    > Affenpinscher, Ca Mè Mallorquí, Old Croatian Sighthound 컬럼 제거
    ```bash
    print(f"중복된 행 개수: {df2.duplicated().sum()}")
    df2[df2.duplicated()]
    df2 = df2.drop(index=[1, 78, 443], ).reset_index(drop=True)    
    ```
    
- ##### 2. 품종 이름이 영어가 아닌 다른언어가 있어서 결합이 안되는 문제 발생
    
    > Bichon Frisé -> Bichon Frise
    
    > Löwchen -> Lowchen

    > Petit Basset Griffon Vendéen -> Petit Basset Griffon Vendeen
    ```bash
    df2['품종'] = df2['품종'].replace({
    'Bichon Frisé':'Bichon Frise',
    'Löwchen':'Lowchen',
    'Petit Basset Griffon Vendéen':'Petit Basset Griffon Vendeen',
    })
    ```

- ##### 3. 품종은 같으나, 기준데이터 `Dog Breed Around The World.csv`와 이름이 다르게 기입되어 있음

    > American Eskimo Dog -> American Eskimo
    
    > Chinese Crested Dog -> Chinese Crested
    
    > Shar Pei -> Chinese Shar-Pei
    
    > Dobermann -> Doberman Pinscher
    
    > Bulldog -> English Bulldog
    ```bash
    df2['품종'] = df2['품종'].replace({
    'American Eskimo Dog':'American Eskimo',
    'Chinese Crested Dog':'Chinese Crested',
    'Shar Pei':'Chinese Shar-Pei',
    'Dobermann':'Doberman Pinscher',
    'Bulldog':'English Bulldog',
    })
    ```

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
    ```bash
    df['품종'] = df['품종'].replace({
    'Cocker Spaniel':'American Cocker Spaniel',
    'Collie':'Rough Collie',
    'Mastiff':'English Mastiff'
    })
    ```

- ##### 2. 평균 체중의 값이 25-Jul 로 잘못 표기되어있음
    > 25-Jul은 25~7kg 범위를 의미함

    > 평균값으로 수동으로 데이터 변환 -> 16
    ```bash
    df["크기 수치화"] = df["크기"].apply(lambda x: sum(size_mapping[s] for s in x) / len(x))
    ```

---
## 📌 데이터셋 출처/품종 정보 출처

데이터셋(캐글)
                
https://www.kaggle.com/
> https://www.kaggle.com/datasets/edoardoba/dog-breeds
            
> https://www.kaggle.com/datasets/prajwaldongre/top-dog-breeds-around-the-world
            
직접 추가한 품종 링크, 이미지의 출처
            
> https://www.akc.org/



