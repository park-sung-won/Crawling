# 메타버스 최초 크롤링데이터
df = pd.read_csv("파일명.csv")

# 특정 컬럼 유니크 값 개수 확인 >> 불필요한 컬럼 제거 목적
df["createdAt"].value_counts()

# 한국 서울 주소지 값만 추출
df_korea = df[df["address"].str.contains("Seoul")==True]
df_korea.head(1)

# 구별로 나타내기
df_gu_list = df_korea["address"].to_list()

a = []
for i in range(len(df_gu_list)):
    gu_list = df_gu_list[i].split()[3]
    a.append(gu_list)

df_korea["gu_address"] = a
df_korea.head(1)

# 센트 > 달러 > 원 단위 환산
df_korea["totalPrice/100*1200"] = df_korea["totalPrice"]/100*1200
df_korea["boughtPrice/100*1200"] = df_korea["boughtPrice"]/100*1200
df_korea.head(1)

# 불필요한 컬럼 제거
df_1 = df_korea.drop(["uuid","Unnamed: 0","sellOrderId","allSellOrdersCount","lastPage","currentPage","currentSellOrderCount","isMyTile","sellerReferralCode"], axis = 1)
df_1.head(1)


# 필요한 컬럼 추출 : 메타버스 시장가격 (단위 : 센트>달러>원 , 고정환율 : 1,200원)
df_meta = pd.DataFrame()
df_meta["boughtPrice"] = df_1["boughtPrice/100*1200"]
df_meta["totalPrice"] = df_1["totalPrice/100*1200"]
df_meta["gu_address"] = df_1["gu_address"]
df_meta["dong_address"] = df_1["memo"]

# df_meta_index = df_meta.set_index(['gu_address','dong_address'])
df_meta
