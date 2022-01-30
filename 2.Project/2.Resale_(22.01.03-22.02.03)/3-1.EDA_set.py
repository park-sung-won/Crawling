import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split

from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression
import xgboost as xgb



# 데이터 불러오기
df = pd.read_csv("./데이터파일.csv")
df = df.dropna()
df.info()

# 필요없는 컬럼 제거
df = df.drop(["name", "num","day", "day1","col"], axis = 1)

# 이상치 제거 1  => 좀 더 자세한 EDA 과정 
out = ((df['min']-df['price'])/df['price'] * 100)  # (현재 - 과거) / 과거
out.describe()

a = out.describe().tolist()[4]
b = out.describe().tolist()[6]

top = b + 1.5*(b-a)    # 1% 이상치
bottom = a - 1.5*(b-a)

df = df[(out <= top) & (out >= bottom)]
df
