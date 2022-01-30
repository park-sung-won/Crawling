## 라벨 인코딩


# from sklearn.preprocessing import LabelEncoder

# # 색상 1
# items = df["col1"] # 컬럼

# label = LabelEncoder()
# label_encoder = label.fit(items)
# labels = label_encoder.transform(items)
# df_label_col1 = pd.DataFrame(labels, columns = ["col1_label"])# column = [""]

# # 색상 2
# items = df["col2"] # 컬럼

# label = LabelEncoder()
# label_encoder = label.fit(items)
# labels = label_encoder.transform(items)
# df_label_col2 = pd.DataFrame(labels, columns = ["col2_label"])# column = [""]

# df_label_col = pd.concat([df_label_col1,df_label_col2], axis = 1)
# df_label_col
