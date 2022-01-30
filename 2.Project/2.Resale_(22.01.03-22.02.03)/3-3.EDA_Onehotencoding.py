# 원핫인코딩 => 컬럼 값 숫자로 변경



# 색상값 1
df_col1 = pd.get_dummies(df['col1'], prefix = 'col1')
df_col2 = pd.get_dummies(df['col2'], prefix = 'col2')
df_col_1 = pd.concat([df_col1 , df_col2], axis =1)

# 카테고리
df_category = pd.get_dummies(df['category'], prefix = 'category')

# 로우하이
df_high_low_mid = pd.get_dummies(df['high/low'], prefix = 'high/low/mid')

# 브랜드
df_brand = pd.get_dummies(df['brand'], prefix = 'brand')

# line
df_line = pd.get_dummies(df['line'], prefix = 'line')

# 성별
df_sex = pd.get_dummies(df['W1M0'], prefix = 'W1M0')

df_final_p = pd.concat([df_col_1, df_category, df_high_low_mid, df_brand, df_line, df_sex], axis =1)
#####df_final_p = pd.concat([df_category, df_high_low_mid, df_brand, df_line, df_sex], axis =1)


df_copy = df.copy().drop(["col1","col2","brand","category","high/low","W1M0","line"], axis = 1)
#####df_copy = df.copy().drop(["brand","category","high/low","W1M0","line"], axis = 1)


df = pd.concat([df_copy, df_final_p], axis = 1)

data = df.drop("min", axis = 1)

data.head(1) # 타겟값 제외한 데이터프레임
df['min'].head(1) # 타겟값
