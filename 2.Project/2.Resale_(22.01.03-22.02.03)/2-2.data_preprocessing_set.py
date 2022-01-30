## 데이터 전처리
### 0. 데이터 불러오기
### 1. 발매일 이후 30일 이내의 거래일자가 10개 미만인 경우는 제외
### 2. 발매일 이후 30일 이내 상품의 최저가격 찾기
### 3. 가격데이터가 잘못 표기된 가격데이터 전처리

name = []
date1 = []
price1 = []
price2 = []
price3 = []
min_list = []
df_emp = pd.DataFrame()

for a in data_jordan_1_high_270:
    df_pro_n = pd.read_csv(f"./1.data_process/3.jordan_1_high/{a}")  # 신발 가격데이터 불러오기 (컬럼 : 날짜, 가격)

#### 데이터 10개 미만인 것은 제외
    if df_pro_n.iloc[0:30].isnull()["price"].sum() > 20:
        
        min_list.append(np.nan)
        name.append(a)
        date1.append(df_pro_n["buy"][0])
        price1.append(df_pro_n["price"][0])
        price2.append(df_pro_n["price"][1])
        price3.append(df_pro_n["price"][2])

    elif df_pro_n.iloc[0:30].isnull()["price"].sum() <= 20:
        min_list.append(df_pro_n.iloc[0:30]["price"].min())
        name.append(a)
        date1.append(df_pro_n["buy"][0])
        price1.append(df_pro_n["price"][0])
        price2.append(df_pro_n["price"][1])
        price3.append(df_pro_n["price"][2])


df_emp["name"] = name
df_emp['date1'] = date1
df_emp['price1'] = price1
df_emp['price2'] = price2
df_emp['price3'] = price3
df_emp['min'] = min_list 



### 가격이 잘못표기되어 있는 데이터 전처리 
# ** 가끔씩 가격표기가 잘못되어있는 데이터가 존재하였음 ex. 실제가격 1,500,000 -> 오류데이터 1,500
for i in range(len(df_emp["name"])):  
    if df_emp["price1"][i] < 10000 :
        df_emp["price1"][i] = df_emp["price1"][i]*1000

    if df_emp["price2"][i] < 10000 :
        df_emp["price2"][i] = df_emp["price2"][i]*1000        

    if df_emp["price3"][i] < 10000 :
        df_emp["price3"][i] = df_emp["price3"][i]*1000

    if df_emp["min"][i] < 10000:
        df_emp["min"][i] = df_emp["min"][i]*1000

#df_emp.round() ### 소수점 반올림
df_data = df_emp.round()
df_data_f = df_data.copy().drop(["min"],axis = 1).fillna(method='ffill',axis = 1)

df_data_f["min"] = df_data["min"]
df_jordan_1_high_man = df_data_f.dropna()

df_jordan_1_high_man.to_csv(f"./0.data/jordan_1_high_man.csv")

df_jordan_1_high_man
