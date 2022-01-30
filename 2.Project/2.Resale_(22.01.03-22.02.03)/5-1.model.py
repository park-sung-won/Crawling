
X = data.to_numpy()
y = df['min'].to_numpy()

from sklearn.model_selection import train_test_split

# 70프로를 트레이닝 셋, 30프로를 테스트 셋
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=123) 
# 70% training and 30% test
