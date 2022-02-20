## 가설 검증을 위한 데이터 전처리

###################################################D50#####

# 거래량 필터링
# df_max = pd.DataFrame()
name_list = []
max_list = []

for i in item_crawl_all:
    if i != '.DS_Store': # 맥 파일이름 리스트에서 제외
        df = pd.read_csv(f'./0.data_crawl/0.all_crawl/{i}')
        
        if len(df) >= 30: # 거래량 (행의 수)
    
            for a in range(len(df["price"])): # 데이터 전처리
                df["price"][a] = df["price"][a].split('원')[0].split(',')[0] + df["price"][a].split('원')[0].split(',')[1]

            df["price"] = df["price"].astype('float')
            df = df.groupby(by = "buy").mean()#.drop("Unnamed: 0", axis = 1).drop('size', axis = 1)
            
            if len(df) > 5: #10일, 20일, 30일, 40일, 50일 단위로 범위 설정하여 최고점 형성 분포 확인
                
                
                df_10 = df.copy().iloc[:50].reset_index(drop = False , inplace = False)
                                      # 보고 싶은 범위 : 50
                name_list.append(i)
                max_list.append(df_10.index[df_10['price'] == df_10['price'].max()].tolist()[0])
                

                df_max_50 = pd.DataFrame()               
                df_max_50['name'] = name_list
                df_max_50['max'] = max_list
#                 print(i)
#                 print(df_10.index[df_10['price'] == df_10['price'].max()].tolist())
                
df_max_50

df_max_50.hist()
