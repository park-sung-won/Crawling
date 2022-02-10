# 타겟값에 영향을 주지 않는다고 가정하여 불필요한 피쳐를 버리는 것 

# 3가지 방법이 존재
# 1. Filtering Method
#  - Filtering은 사전적 의미 처럼 도움이 되지 않는 피처들을 걸러내는 작업을 말합니다.  통계적인 측정 방법을 이용하여 피처들의 상관관계를 알아내고 적합한 피처들만 선택하여 알고리즘에 적용하는 방식입니다.

# ** 대표적인 방법은 아래와 같습니다 
# - t-test
# - chi-square test
# - Information Gain

# 2. Wrapper Method
#  - wrapper는 예측 모델을 사용하여 피처들의 부분 집합을 만들어 계속 테스트 하여 최적화된 피처들의 집합 만드는 방법 입니다. 최적화된 모델을 만들기 위해 여러번 모델을 생성하고 성능을 테스트 해야 하기 때문에 많은 시간이 필요합니다. 충분한 시간이 있다고 하면 wrapper 방법을 사용해도 좋지만 시간이 없다면 다른 방법을 사용하는 것을 추천합니다.
 
# ** 대표적인 방법에는 다음과 같습니다

# - Forward Greedy
# - Backward Greedy
# - Genetic Search
# - Local Search

# 3. Embedded Method
#  - Embedded는 Filtering과 Wrapper의 장점을 결함한 방법으로 학습 알고리즘 자체에 feature selection을 넣는 방식입니다.

# ** 대표적인 방법은 다음과 같습니다.

# - LASSO = L1 regularisation
# - RIDGE = L2 regularisation


# 출처 : https://firework-ham.tistory.com/48
######################################################
## 1. Filtering Method

df_corr = pd.concat([data,df["min"]], axis =1).corr().tail(1)
df_corr[abs(df_corr > 0.5)]


