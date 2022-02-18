## 다중선형회귀분석

from sklearn.linear_model import LinearRegression
mlr = LinearRegression()
mlr.fit(X_train, y_train) 

y_predict = mlr.predict(X_test)

import matplotlib.pyplot as plt
plt.scatter(y_test, y_predict, alpha=0.4)
plt.xlabel("Actual min")
plt.ylabel("Predicted min")
plt.title("MULTIPLE LINEAR REGRESSION")
plt.show()

# plt.scatter(df[['price']], df[['min']], alpha=0.4)
# plt.scatter(df[['price1']], df[['min']], alpha=0.4)
# plt.scatter(df[['price2']], df[['min']], alpha=0.4)
# plt.scatter(df[['price3']], df[['min']], alpha=0.4)

# plt.show()

print(mlr.coef_)

print(mlr.score(X_train, y_train))

from sklearn.metrics import mean_squared_error
rmse = np.sqrt(mean_squared_error(y_test, y_predict))
print("RMSE: %f" % (rmse))


# # 시각화

# X_data = X_train
# Y_data = y_train

# linear_regression_model = mlr
# linear_regression_model.fit(X = pd.DataFrame(X_data), y = Y_data)
# linear_regression_model_prediction = mlr.predict(X = pd.DataFrame(X_test))

# fig = plt.figure(figsize = (12,4))
# gragh = fig.add_subplot(1,1,1)
# gragh.plot(Y_data[:30], marker='o', color = 'blue', label = '실제값')
# gragh.plot(linear_regression_model_prediction[:30], marker='^', color = 'red', label = '예측값' )
# gragh.set_title('다중회귀분석 예측결과', size = 30)
# plt.xlabel('횟수', size = 20)
# plt.ylabel('최저', size = 20)
# plt.legend(loc = 'best')
