## XGBoost 

import xgboost as xgb
from sklearn.metrics import mean_squared_error
import pandas as pd
import numpy as np

xg_reg = xgb.XGBRegressor(n_estimators = 16,alpha = 179, colsample_bytree = 0.99,max_depth = 6, learning_rate = 0.3, subsample = 0.918)

# # xg_reg = xgb.XGBRegressor(objective ='reg:linear', colsample_bytree = 0.3, learning_rate = 0.1,
# #                 max_depth = 5, alpha = 10, n_estimators = 10)
# xg_reg = xgb.XGBRegressor(objective ='reg:linear', n_estimators = 195,learning_rate = 0.2, max_depth = 3)

xg_reg.fit(X_train,y_train)
preds = xg_reg.predict(X_test)

y_true = y_test.copy()
y_pred = preds.copy()

print('Mean Absolute Percentage Error (MAPE):', metrics.mean_absolute_percentage_error(y_true, y_pred))

rmse = np.sqrt(mean_squared_error(y_test, preds))
print("RMSE: %f" % (rmse))

xgb.plot_importance(xg_reg)
plt.rcParams['figure.figsize'] = [30, 30]
plt.show()

