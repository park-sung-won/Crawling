# 실제 부동산 토지 공시지가 데이터 전처리

# 현실 공시지가 데이터  
# (출처 : http://stat.molit.go.kr/portal/cate/statView.do?hRsId=25&hFormId=6214&hSelectId=6214&sStyleNum=1&sStart=2020&sEnd=2020&hPoint=0&hAppr=1&oFileName=&rFileName=&midpath=)

df_real = pd.read_excel("01.토지_소유구분별_기본_현황_시군구.xlsx")

df_real = df_real[["시도", "시군구","합 계", "Unnamed: 3","Unnamed: 4"]]
df_real.columns = ["시도","시군구","면적", "지번수","가액"]
df_real = df_real.iloc[3:28, 0:6].fillna("서울특별시")

#공식 : 가액 = 면적 * (지분) * 개별공시지가 * 50/100   (국유지랑 사유지가 모두 포함되어 있기 때문에, 지분은 1로 계산함)
#따라서, 가액 * 2 / 면적 = 개별공시지가


# df_real 데이터 프레임의 단위 > 면적 : km^2 , 가액 : 10억원
# 면적 단위 km^2 > m^2 로 맞추기
df_real["면적"] = df_real["면적"] * 1000000


# 개별공시지가 (단위 : 10억원)
df_real["개별공시지가"] = df_real["가액"] * 2 / df_real["면적"]
df_real["TP"] = df_real["가액"] * 2
df_real

