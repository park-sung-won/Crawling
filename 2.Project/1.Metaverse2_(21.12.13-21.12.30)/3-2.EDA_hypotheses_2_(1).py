# 가설 수립 - 2
## 가설2 : [서울] 메타버스2 서비스의 '랜드마크'라는 서비스 요인이 가상부동산 가격형성에 영향을 준다.

## 서비스 요인 3가지 
# 1) 메타버스2의 서비스 요인 분석 : 확정 랜드마크
# 2) 메타버스2의 서비스 요인 분석 : 랜드마크 예상 기대지역
# 3) 메타버스2의 서비스 요인 분석 : 랜드마크(확정/예상)가 가격형성에 미치는 영향





# 메타버스2의 서비스 요인 분석 : 확정 랜드마크

#* 실제 서울시 면적 : 605km^2 = 650000000m^2
#* 실제 뉴욕시 면적 : 1214.4km^2 = 1214400000m^2
#* 실제 서울시 면적 : 실제 뉴욕시 면적 = 1 : 1.87

# 메타버스2 가상부동산 서울시 전체 TP
df_meta["totalPrice"].sum()

# 메타버스2 가상부동산 서울시 랜드마크가 속한 구 TP
a_gu = df_meta[df_meta["gu_address"] == "Jung-gu"]["totalPrice"].sum() # 2598203928 원
b_gu = df_meta[df_meta["gu_address"] == "Yongsan-gu"]["totalPrice"].sum()  # 2825548392 원
c_gu = df_meta[df_meta["gu_address"] == "Seongdong-gu"]["totalPrice"].sum()  # 825924732 원
d_gu = df_meta[df_meta["gu_address"] == "Songpa-gu"]["totalPrice"].sum()  # 5490518904 원
e_gu = df_meta[df_meta["gu_address"] == "Jongno-gu"]["totalPrice"].sum()  # 5294590824 원

land_sum_gu = a_gu + b_gu + c_gu + d_gu + e_gu
land_sum_gu

land_sum_gu / df_meta["totalPrice"].sum() * 100
#* 메타버스2 서울시 전체 25개구 중, 가상부동산 가격의 약 60%가 랜드마크가 속한 5개에서 나타남.  

# 메타버스2 서울시 확정 랜드마크 8개 TP
# 메타버스2 서울시내 랜드마크가 있는 구 : 중구, 용산구, 성동구, 송파구, 종로구 (총 5곳) 

df_land_gu_sum = {}
df_land_gu_sum["중구_TP"] = df_meta[df_meta["gu_address"] == "Jung-gu"]["totalPrice"].sum() # 2598203928 원
df_land_gu_sum["용산구_TP"] = df_meta[df_meta["gu_address"] == "Yongsan-gu"]["totalPrice"].sum()  # 2825548392 원
df_land_gu_sum["성동구_TP"] = df_meta[df_meta["gu_address"] == "Seongdong-gu"]["totalPrice"].sum()  # 825924732 원
df_land_gu_sum["송파구_TP"] = df_meta[df_meta["gu_address"] == "Songpa-gu"]["totalPrice"].sum()  # 5490518904 원
df_land_gu_sum["종로구_TP"] = df_meta[df_meta["gu_address"] == "Jongno-gu"]["totalPrice"].sum()  # 5294590824 원

df_land_gu_tp = pd.DataFrame([df_land_gu_sum]) # 랜드마크가 속한 지역구 TP
df_land_gu_tp


# 랜드마크
landmark = pd.read_csv("2.확정랜드마크_데이터셋.csv")
landmark

# 확정랜드마크가 속한 구에서 산,강 요인에 대한 데이터 셋
land_tree = pd.read_csv("1.랜드마크(구)_산,강_데이터.csv", encoding = "cp949")
land_tree

## 서비스 요인별 메타버스2 가상부동산 가격형성에 영향을 미치는 정도를 파악하기 위해 1)랜드마크 와 2)산,강 각각의 서비스 요인은 분리해서 분석함

# 서울 전체 TP 중, 랜드마크가 차지하는 점유율 약 41%
landmark["TP_원"].sum() / df_meta["totalPrice"].sum() * 100

# 서울 전체 면적 중, 랜드마크가 차지하는 점유율 약 0.08%
landmark["타일 수"].sum() / (3025000) * 100


#메타버스2 가상부동산 내에서 랜드마크가 차지하는 면적대비 TotalPrice를 확인해봤을때,
#랜드마크가 메타버스2에서 서비스 요인으로서 약512.5배이상으로 작용한다는 것을 알 수 있음
