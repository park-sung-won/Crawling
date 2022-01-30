## 신발카테고리별 데이터 저장


df2 = pd.read_csv("./0.data/text_jordan_1_high.csv")

df2["day"] = pd.to_datetime(df2["day"],yearfirst = True)

for a in range(len(df2["price"])):
    df2["price"][a] = df2['price'][a].split("원")[0].split(" ")[-1].split(',')[0] + df2['price'][a].split("원")[0].split(" ")[-1].split(',')[1]

# wish int 타입으로 변경
for a in range(len(df2['wish'])):
    if len(df2['wish'][a]) == 4:
        df2['wish'][a] = int(df2['wish'][a].split('만')[0].split('.')[0] + df2['wish'][a].split('만')[0].split('.')[1]) * 1000
        
    elif len(df2['wish'][a]) == 5:
        df2['wish'][a] = int(df2['wish'][a].split(',')[0] + df2['wish'][a].split(',')[1])

df2.head()



# 데이터 조던 1 로우 
df = pd.read_csv("./0.data/jordan_1_high_man.csv")

for i in range(len(df["name"])):
    df["name"][i] = df["name"][i].split(".")[0]
    
df1 = df.drop("Unnamed: 0", axis = 1)
df1.head()


# 저장하기
df_price_text = pd.merge(df1,df2, how='outer', on='name')
df_price_text.to_csv("./2.data_price_text/jordan_1_high_M.csv")
