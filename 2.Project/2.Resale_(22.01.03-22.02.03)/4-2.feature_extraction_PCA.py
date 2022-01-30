# 추출 -> 선택하는 것이 아니라 더 작은 차원으로 feature 를 맵핑하는 것
# - 차원 축소 기법에는 PCA, LDA, SUD, NMF 가 있음



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


## scree_plot 
def scree_plot(pca):
    num_components = len(pca.explained_variance_ratio_)
    ind = np.arange(num_components)
    vals = pca.explained_variance_ratio_
    
    ax = plt.subplot()
    cumvals = np.cumsum(vals)
    ax.plot(ind, cumvals, color = '#b4cccc')
    ax.bar(ind, vals, color = ['#ffa6b6', '#ffc67a',  '#b3ff70', '#66faf7', '#c591ff'])
    for i in range(num_components):
        ax.annotate(r"%s" % ((str(vals[i]*100)[:3])), (ind[i], vals[i]), va = "bottom", ha = "center", fontsize = 13)
     
    ax.set_xlabel("Number of PC")
    ax.set_ylabel("Variance")
    plt.title('Scree plot')
    
scree_plot(pca)
