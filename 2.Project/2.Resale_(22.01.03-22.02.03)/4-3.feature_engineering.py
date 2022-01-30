# 생성
# *Feature Engineering

# 1. Feature Selection
# - 결과값에 유효한 영향들을 미치는 Feature 값을 임의로 선택하여 머신러닝 성능을 향상시킨다.
# (상관 분석을 통하여 유효값의 기준 및 범위를 세울 수 있다.)

 
# 2. Feature Nomalization(정규화)
# - Feature마다 서로 다른 범위를 가지고 있을 때 값이 발생시키는 유효성의 차이가 생길 수 있음
# - 차이를 최소화 하여 성능을 향상시키는 방법

# 1) Standardization(표준화)
# - 범위값(Numerical Column)의 각기 다른 범위를 정규분포표를 만들어 사용
# from sklearn import preprocessing 
# normalized_data=preprocessing.StandardScaler().fit_transform(data)

# 2) Min-Max Scaler
# - 최소값과 최댓값사이를 범위로 한 정규화방법 (0~1사이에 위치함)

# from sklearn import preprocessing 
# normalized_data = preprocessing.MinMaxScaler().fit_transform(data)

# 3. Feature Generation
# - 여러개의 Feature를 조합하여 새로운 Feature를 만드는 방법
# - PolynomialFeatures : 서로 다른 Feature들 간의 곱셈으로 새로운 Feature를 만든다.

# from sklearn.preprocessing import MinMaxScaler, PolynomialFeatures 
# X=MinMaxScaler().fit_transform(Data) 
# X=PolynomialFeatures(degree=2, include_bias=False).fit_transform(X)

# 출처: https://scarlett-choi.tistory.com/45 [스칼렛의 코딩라이프]





import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


df = data
df.shape

plt.figure(figsize=(8,4))
plt.xticks(range(0, 30000, 1000), rotation=60)
sns.distplot(df['price1'])





import seaborn as sns
import matplotlib.pyplot as plt

# 변수(price1)에 log변환을 취해서 분포도 변환시킨후 학습시키기
def get_preprocessed_df(df):
    df_copy = df.copy()
    amount_n = np.log1p(df_copy['price1'])
    df_copy.insert(0, 'price1_log', amount_n)
    df_copy.drop(['price1'], axis=1, inplace=True)
    return df_copy
    
card_df = get_preprocessed_df(df)

plt.figure(figsize=(8,4))
plt.xticks(range(0, 30000, 1000), rotation=60)
sns.distplot(df['price1_log'])



# 이상치 제거후 모델 학습 평가
# 우선 타겟값과 상관관계가 높은 변수를 기준으로 이상치를 제거
# 이를 위해 상관관계 살펴보기
plt.figure(figsize=(10,8))

corr = df.corr()
sns.heatmap(corr, cmap='Blues')





##################################################
# 가장 상관관계가 높은 변수의 이상치를 제거해보자.

# weight값은 이상치에 포함되는 범위 결정할 때 곱해주는 계수값
def get_outlier(df, column, weight=1.5):
  
    fraud = df[df['min'] ==1][column]
    quantile_25 = np.percentile(fraud.values, 25)
    quantile_75 = np.percentile(fraud.values, 75)
    
    # IQR을 구하고 1.5를 곱해서 이상치 포함시킬 범위 정의
    iqr = quantile_75 - quantile_25
    iqr_w = iqr * weight
    lowest = quantile_25 - iqr_w
    highest = quantile_75 + iqr_w
    
    outlier_idx = fraud[(fraud < lowest) | (fraud > highest)].index
    
    return outlier_idx

  
outlier_idx = get_outlier(df, 'price1')
df_copy.drop(outlier_idx, axis=0, inplace=True)

