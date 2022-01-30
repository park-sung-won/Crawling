# PCA (차원축소)


# 전체데이터

## 표준화
from sklearn.preprocessing import StandardScaler  # 표준화 패키지 라이브러리 
x = data.values # 독립변인들의 value값만 추출
y = df['min'].values # 종속변인 추출

x = StandardScaler().fit_transform(x) # x객체에 x를 표준화한 데이터를 저장

features = df.drop(['min'], axis=1).columns.to_list()
pd.DataFrame(x, columns=features).head()

## PCA
from sklearn.decomposition import PCA
pca = PCA(n_components=5) # 주성분을 몇개로 할지 결정
printcipalComponents = pca.fit_transform(x)
principalDf = pd.DataFrame(data=printcipalComponents) #columns = ['principal component1', 'principal component2']
# 주성분으로 이루어진 데이터 프레임 구성

principalDf.head()
pca.explained_variance_ratio_
sum(pca.explained_variance_ratio_) 
