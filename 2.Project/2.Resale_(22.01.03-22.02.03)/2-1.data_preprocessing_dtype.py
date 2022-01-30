## 크롤링 데이터 타입변환


ls 0.data_crawl/3.JD_1_high_M.  # 파일경로에 있는 파일 이름 조회
                                # item_JD_high_list : 크롤링 파일 이름 리스트


for i in item_JD_high_list:
    df = pd.read_csv(f'./0.data_crawl/3.JD_1_high_M/{i}')
    
    for a in range(len(df["price"])):
        df["price"][a] = df["price"][a].split('원')[0].split(',')[0] + df["price"][a].split('원')[0].split(',')[1]

    df["price"] = df["price"].astype('float')
    df['buy'] = pd.to_datetime(df['buy'], yearfirst=True)
    df = df.groupby(by = "buy").mean().drop("Unnamed: 0", axis = 1).drop('size', axis = 1)
    df = df.resample('D').mean()
    
    print(df)
    df.to_csv(f"./1.data_process/3.jordan_1_high/{i.split('_')[1]}.csv") # 파일이름 정제함
    
