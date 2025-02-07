# 🐶 Dog Info App

**Dog Info App** 은 강아지 품종 추천과 가격, 건강, 수명 예측 기능을 제공하는 Streamlit 기반 웹 애플리케이션입니다.

## 🚀 주요 기능
### 1. 🏠 홈

- 앱 소개 및 기능 설명을 확인할 수 있습니다.

### 2. 🐕 강아지 추천

- 사용자의 선호도와 데이터를 기반으로 KNN 모델을 활용하여 적절한 강아지 품종을 추천합니다.

### 3. 📈 데이터 분석

- 강아지 가격, 건강, 수명을 예측하는 회귀 모델을 제공합니다.

- K-Means 클러스터링을 활용한 반려견 유형 분석 기능을 포함합니다.

- Collaborative Filtering을 이용한 추천 시스템 기능을 제공합니다.

---

## 📂 데이터셋

- dogs-ranking-dataset.csv 파일을 사용하여 강아지 품종별 다양한 정보를 분석합니다.

- 주요 컬럼: 품종, 유형, 점수, 인기순위, 지능, 선천적질병, 수명(년), 평균구매가격, 연간 사료비용 등

---
## 🔧 기술 스택

- Frontend: Streamlit

- Backend: Python (Pandas, Scikit-learn)

- Machine Learning: KNN, Decision Tree, Regression, K-Means, Collaborative Filtering

- 데이터 시각화: Matplotlib, Seaborn

---
📌 실행 방법
```bash
# 필수 라이브러리 설치
pip install -r requirements.txt

# 애플리케이션 실행
streamlit run app.py
```

---
## 📡 실시간 환율 적용

- 네이버 금융 API를 사용하여 USD → KRW 환율을 실시간으로 반영합니다.

- 최신 환율 확인: 네이버 금융 환율 페이지

---
## 🛠 추가 개선 사항

- 데이터 추가 확보 및 예측 모델 성능 향상

- 사용자 맞춤 추천 기능 고도화

- UI/UX 디자인 개선




