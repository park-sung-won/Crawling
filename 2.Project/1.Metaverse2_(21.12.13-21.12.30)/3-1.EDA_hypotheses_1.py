# 가설 수립 - 1
## 가설1 : [서울] 현실 부동산(토지)가격이 메타버스2 가상부동산 가격형성과 관계가 있다.

df_col = df_real[["TP","시군구"]]
df_col.head(1)


df_col_a = []
for i in ["Jongno-gu", "Jung-gu", "Yongsan-gu", "Seongdong-gu", "Gwangjin-gu", "Dongdaemun-gu", "Jungnang-gu", 
          "Seongbuk-gu", "Gangbuk-gu", "Dobong-gu", "Nowon-gu", "Eunpyeong-gu", "Seodaemun-gu", "Mapo-gu",
          "Yangcheon-gu", "Gangseo-gu", "Guro-gu", "Geumcheon-gu", "Yeongdeungpo-gu", "Dongjak-gu" , "Gwanak-gu", 
          "Seocho-gu", "Gangnam-gu", "Songpa-gu", "Gangdong-gu"]:
    a = df_meta[df_meta["gu_address"] == i]["totalPrice"].sum()
    df_col_a.append(a)
    
df_col["meta_tp"] = df_col_a
df_col.head(1)


# 스케일이 차이가 큰 상태로 시각화할 경우, 데이터를 읽기 어려울 수 있기 때문에 Log를 씌워 데이터 스케일 차이를 줄이고 데이터를 읽기 위함 
df_col["real_tp_log"] = np.log(df_col["TP"])
df_col["meta_tp_log"] = np.log(df_col["meta_tp"])
df_col

sns.scatterplot(data = df_col, x = 'real_tp_log', y = 'meta_tp_log')

sns.regplot(data = df_col, x = 'real_tp_log', y = 'meta_tp_log')


plt.figure(figsize=(12,6))
sns.barplot(data = df_col, x = '시군구', y = 'meta_tp') 
plt.xticks(rotation=90)
# barplot은 로그값을 적용한 데이터로 시각화할 경우에 읽기 어려움


plt.figure(figsize=(12,6))
sns.barplot(data = df_col, x = '시군구', y = 'TP') # barplot은 로그값을 적용한 데이터로 시각화할 경우에 읽기 어려움
plt.xticks(rotation=90)



## 스피어만 상관분석 진행
df_rank = pd.DataFrame()

df_rank["meta"] = df_col['meta_tp_log'].rank(method='max', ascending=False)
df_rank["real"] = df_col['real_tp_log'].rank(method='max', ascending=False)
df_rank["gu"] = df_col["시군구"]

df_rank

A = df_rank["meta"]
B = df_rank["real"]

stats.spearmanr(A, B)

# [학습출처] https://hyen4110.tistory.com/38
# [학습출처] https://bskyvision.com/754


#현실의 부동산 토지가격과 메타버스2 가상부동산 토지의 가격을 상관분석했을때, 0.83의 상관관계를 알 수 있음
#즉, 어느정도 현실의 부동산 토지가격과 메타버스2 가상부동산 토지의 가격이 서로 연관성이 있다는 것을 알 수 있다.

## 자세히 살펴보기 위해, 현재 메타버스2 플랫폼 내에서의 서비스 요인인 랜드마크를 제거하고 상관분석 진행




# 랜드마크 요인 제거
df_col_land = df_col.copy()
df_col_land.drop(["meta_tp_log"], axis = 1)

# 1)현재서비스요인 : 랜드마크 , 2)향후서비스요인 : 산, 강 > 2가지 요인을 모두 제외한 TP (랜드마크가 속한 5개 구)
df_col_land.loc[df_col_land['시군구'] == "중구", 'meta_tp'] = 1.406463e+09 
df_col_land.loc[df_col_land['시군구'] == "용산구", 'meta_tp'] = 9.144154e+08
df_col_land.loc[df_col_land['시군구'] == "성동구", 'meta_tp'] = 3.960063e+08
df_col_land.loc[df_col_land['시군구'] == "송파구", 'meta_tp'] = 1.667442e+09
df_col_land.loc[df_col_land['시군구'] == "종로구", 'meta_tp'] = 2.362390e+09


df_col_land["meta_tp_log_land"] = np.log(df_col_land["meta_tp"])
df_col_land
# df_col_landmin["meta_tp_log_min"] = np.log(df_col_landmin["meta_tp"])
# df_col_landmin

sns.scatterplot(data = df_col_land, x = 'real_tp_log', y = 'meta_tp_log_land')

df_rank_land = pd.DataFrame()

df_rank_land["meta_land"] = df_col_land['meta_tp_log_land'].rank(method='max', ascending=False)
df_rank_land["real_land"] = df_col_land['real_tp_log'].rank(method='max', ascending=False)
df_rank_land["gu"] = df_col_land["시군구"]

df_rank_land

C = df_rank_land["meta_land"]
D = df_rank_land["real_land"]
stats.spearmanr(C, D)


#랜드마크 요인을 빼고 분석한 결과 이전 결과대비 약간 상승한 0.84의 상관관계를 알 수 있음
#즉, 어느정도 현실의 부동산 토지가격과 메타버스2 가상부동산 토지의 가격이
#랜드마크라는 서비스요인을 제외하고도 서로 연관성이 있다는 것을 알 수 있다.

