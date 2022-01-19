# 메타버스2 가상부동산 거래 플랫폼 거래리스트 수집
# 

url = "https://www.metaverse2.com/marketplace" #수집할 URL

driver = webdriver.Chrome("./chromedriver")    #chromedriver 경로 설정
driver.get(url)

df_all = []
for a in trange(1,5286):  # trange : 진행률 확인 , 5286 페이지 수 설정
    time.sleep(2)         # 동작간의 시간 텀
    elements = driver.find_element_by_class_name("column_table03").find_elements_by_class_name("table_body")
    print(len(elements))
    df_list = []
    for b, elem in enumerate(elements):
        time.sleep(2)
        count_num = driver.find_element_by_class_name("column_table03").find_elements_by_class_name("table_body")
        count_num[b].find_element_by_css_selector(".small_button.black_button.mr5").click()
        time.sleep(5)
        
        html = driver.page_source
        soup = bs(html, "html.parser")
        table = soup.find("div", attrs={"class":"row_table"}).find_all("div", attrs = {"class":"table_col"})

        df_1 = {}
        for row in table:
            time.sleep(3)
            x = row.find("span" , attrs = {"class" : "table_head"}).text.strip()
            df_1[x] = []
            y = row.find("span", attrs = {"class" : "table_body"}).text.strip()
            df_1[x].append(y)
            

        time.sleep(1)
        df_series = pd.DataFrame.from_dict(df_1)
        print(df_series)
        df_list.append(df_series)       
        driver.back()
        
    df_frame = pd.concat(df_list).reset_index()
    df_frame.to_csv("./meta_data_page.csv")
    df_all.append(df_frame)
    
    driver.find_element_by_css_selector(".marketplace__PageArrow-b1ubol-2.ckwXMj").click()

df_final = pd.concat(df_all).reset_index()
df_final.to_csv("./meta_data_all.csv")

driver.quit()
