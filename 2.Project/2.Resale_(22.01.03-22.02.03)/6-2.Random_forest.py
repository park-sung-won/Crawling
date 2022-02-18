## 랜덤포레스트 모델

from sklearn.ensemble import RandomForestClassifier

# estimators  : 랜덤 포레스트 안에 만들어지는 의사결정 나무의 갯수
clf = RandomForestClassifier(n_estimators=100)

clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)

from sklearn import metrics
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))

from sklearn.metrics import mean_squared_error
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
print("RMSE: %f" % (rmse))

data_a = [] # x 컬럼

# 영향
feature_imp = pd.Series(clf.feature_importances_, index=data_a).sort_values(ascending=False)
feature_imp

# Commented out IPython magic to ensure Python compatibility.
import matplotlib.pyplot as plt
# %matplotlib inline
plt.figure(figsize=(6,10))
sns.barplot(x=feature_imp, y=feature_imp.index)
plt.xlabel('Feature Importance Score')
plt.ylabel('Features')
plt.title("Visualizing Important Features")
plt.legend()
plt.show()
