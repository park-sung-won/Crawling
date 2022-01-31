# 가설 수립 - 2
## 가설2 : [서울] 메타버스2 서비스의 '랜드마크'라는 서비스 요인이 가상부동산 가격형성에 영향을 준다.

## 서비스 요인 3가지 
# 1) 메타버스2의 서비스 요인 분석 : 확정 랜드마크
# 2) 메타버스2의 서비스 요인 분석 : 랜드마크 예상 기대지역
# 3) 메타버스2의 서비스 요인 분석 : 랜드마크(확정/예상)가 가격형성에 미치는 영향





# 메타버스2의 서비스 요인 분석 : 랜드마크(확정/예상)가 가격형성에 미치는 영향

df_land_gu_tp # 메타버스 랜드마크가 포함된 구 TP
df_land_gu_tp.sum(axis=1)

df_land_gu_tile = pd.DataFrame()

df_land_gu_tile["중구_tile"] = [49800]
df_land_gu_tile["용산구_tile"] = [109350]
df_land_gu_tile["성동구_tile"] = [84200]
df_land_gu_tile["송파구_tile"] = [169400]
df_land_gu_tile["종로구_tile"] = [119550]

df_land_gu_tile.sum(axis=1)

df_land_gu_tp.sum(axis=1) / df_land_gu_tile.sum(axis=1)

# 랜드마크포함된 5개구 TP / 랜드마크포함된 5개구 타일수 = 5개 구별 타일당 가격
df_land_5gu = pd.DataFrame()
land_A = []
land_B = []

for i in df_land_gu_tp:
    a = df_land_gu_tp[i]
    land_A.append(a)
df_land_5gu["land_tp"] = land_A

    
for w in df_land_gu_tile:
    b = df_land_gu_tile[w]
    land_B.append(b)
df_land_5gu["land_tile"] = land_B

df_land_5gu
# df_land_5gu["5개 타일당 가격"] = land_5gu
# df_land_5gu


