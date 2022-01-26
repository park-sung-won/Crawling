############################################################################################################
# 1. 상품 전체 수집
options = webdriver.ChromeOptions()
options.add_argument("headless")
driver = webdriver.Chrome("./chromedriver", options=options)
#driver = webdriver.Chrome("./chromedriver")
driver.get("https://kream.co.kr/search?category_id=1&tag_id[gender]=45&tag_id[sneakers_size]=97&keyword=Air%20Max%201&sort=popular&per_page=40")

driver.find_element_by_xpath('//*[@id="__layout"]/div/div[1]/div[1]/div/ul/li[4]/a').click()

time.sleep(0.5)

login = driver.find_element_by_xpath('//*[@id="__layout"]/div/div[2]/div[1]/div/div[1]/div/input')
login.send_keys("ID")

password = driver.find_element_by_xpath('//*[@id="__layout"]/div/div[2]/div[1]/div/div[2]/div/input')
password.send_keys("PASSWORD")

time.sleep(0.5)
driver.find_element_by_css_selector(".btn.full.solid").click()

# for c in range(0,10):
#     driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)
#     time.sleep(2)

# for w in range(5):                                                                      # 스크롤 횟수 지정 = range(횟수)
#     try:
#         driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")        # 스크롤 명령 
#         print('스크롤 횟수 : ', (w+1))                                                     # 몇번째 스크롤되고 있는지 확인
#     except:
#         pass
#     time.sleep(2.5) 

time.sleep(3)

for i in trange(1,41):   # 해당 페이지 item 넘버
    time.sleep(3)
    driver.find_element_by_xpath(f'//*[@id="__layout"]/div/div[2]/div[5]/div/div[3]/div[1]/div[{i}]').click()

    item = driver.find_element_by_xpath(f'//*[@id="__layout"]/div/div[2]/div[5]/div/div[3]/div[1]/div[{i}]/a/div[2]/div[1]/p[2]').text
    
    time.sleep(2)
    driver.find_element_by_css_selector(".btn.outlinegrey.full.medium").click()

    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="panel1"]/div/div/div[1]/div/div[3]/a/span').click()
    time.sleep(2)
    
    time.sleep(4)
    print(i,':', driver.find_element_by_xpath('//*[@id="__layout"]/div/div[2]/div[1]/div/div[2]/div/div[2]/div/dl').text)
    
    scr1 = driver.find_element_by_xpath('//*[@id="panel1"]/div/div/div[2]')  # 스크롤할 영역지정
    for x in range(10):                                                      # 스크롤 횟수 지정 = range(횟수)
        try:
            driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scr1)  # 팝업창 스크롤 명령 
            print('스크롤 횟수 : ', (x+1))                                                        # 몇번째 스크롤되고 있는지 확인
        except:
            pass
        time.sleep(2.5) 


    elements = driver.find_element_by_class_name("price_body").find_elements_by_class_name("body_list")
    html = driver.page_source
    soup = bs(html, "html.parser")
    table = soup.find("div", attrs={"class":"price_body"}).find_all("div", attrs = {"class":"body_list"})


    size = []
    price = []
    buy = []
    for y in range(len(elements)):
        a = elements[y].text
        if a.split("\n")[2] == "빠른배송":
            size.append(a.split("\n")[0]) # size
            price.append(a.split("\n")[1]) # price
            buy.append(a.split("\n")[3]) # buy_date
        elif a.split("\n")[2] != "빠른배송":
            size.append(a.split("\n")[0]) # size
            price.append(a.split("\n")[1]) # price
            buy.append(a.split("\n")[2]) # buy_date

    df = pd.DataFrame()

    df["size"] = size
    df["price"] = price
    df["buy"] = buy
    df["kind"] = item

    df.to_csv(f"./0.data_crawl/13.Max_1_M/{item}")
    print(df)
    driver.back()
    time.sleep(3)
    
# 전체리스트 첫화면에서 노출되는 상품까지만 수집되는 현상발생 > 화면 스크롤 등으로 하단 추가로딩되는 상품을 노출시키고 수집해야할 것 같다.

    


############################################################################################################
# 2. 개별 상품 수집 URL
driver = webdriver.Chrome("./chromedriver")
driver.get("https://kream.co.kr/products/23829") # 수집하고자하는 상품의 URL 입력

driver.find_element_by_css_selector(".btn.btn_login.solid.medium").click()

time.sleep(0.5)

# 로그인
login = driver.find_element_by_xpath('//*[@id="__layout"]/div/div[2]/div[1]/div/div[1]/div/input')
login.send_keys("ID")

password = driver.find_element_by_xpath('//*[@id="__layout"]/div/div[2]/div[1]/div/div[2]/div/input')
password.send_keys("PASSWORD")

time.sleep(0.3)
driver.find_element_by_css_selector(".btn.full.solid").click()

time.sleep(1)
driver.find_element_by_css_selector(".btn.outlinegrey.full.medium").click()

time.sleep(1) # 사이즈 클릭
driver.find_element_by_xpath('//*[@id="__layout"]/div/div[2]/div[1]/div/div[2]/div/div[6]/div/div[2]/div[1]/div[2]/div/div/button/span').click()

time.sleep(1) 

# 특정 사이즈 선택
#####
#240부터일때  
#driver.find_element_by_xpath('//*[@id="__layout"]/div/div[2]/div[1]/div/div[2]/div/div[6]/div/div[2]/div[1]/div[2]/div/div/div/div/div[2]/ul/li[8]/a').click()

#230부터일때
#driver.find_element_by_xpath('//*[@id="__layout"]/div/div[2]/div[1]/div/div[2]/div/div[6]/div/div[2]/div[1]/div[2]/div/div/div/div/div[2]/ul/li[12]/a').click()

#220
#driver.find_element_by_xpath('//*[@id="__layout"]/div/div[2]/div[1]/div/div[2]/div/div[6]/div/div[2]/div[1]/div[2]/div/div/div/div/div[2]/ul/li[12]/a').click()

#215
driver.find_element_by_xpath('//*[@id="__layout"]/div/div[2]/div[1]/div/div[2]/div/div[6]/div/div[2]/div[1]/div[2]/div/div/div/div/div[2]/ul/li[13]/a').click()

#####

time.sleep(1)
driver.find_element_by_xpath('//*[@id="panel1"]/div/div/div[1]/div/div[3]/a/span').click()
time.sleep(0.5)

# import datetime
# def doScrollDown(whileSeconds):
#         start = datetime.datetime.now()
#         end = start + datetime.timedelta(seconds=whileSeconds)
#         while True:
#             driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
#             time.sleep(1)
#             if datetime.datetime.now() > end:
#                 break

scr1 = driver.find_element_by_xpath('//*[@id="panel1"]/div/div/div[2]')  # 스크롤할 영역지정
for i in trange(60):                                                     # 스크롤 횟수 지정 = range(횟수)
    try:
        driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scr1)  # 팝업창 스크롤 명령 
        print(i)                                                                           # 몇번째 스크롤되고 있는지 확인
    except:
        pass
    time.sleep(2.5) 

# while True:
#     driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scr1)
#     time.sleep(2)
#     continue


elements = driver.find_element_by_class_name("price_body").find_elements_by_class_name("body_list")
html = driver.page_source
soup = bs(html, "html.parser")
table = soup.find("div", attrs={"class":"price_body"}).find_all("div", attrs = {"class":"body_list"})

df_list = []
for x in range(len(elements)):
    a = elements[x].text
    df_list.append(a)
    
    size = []
    price = []
    buy = []
    for y in range(len(df_list)):
        if df_list[y].split("\n")[2] == "빠른배송":
            size.append(df_list[y].split("\n")[0]) # size
            price.append(df_list[y].split("\n")[1]) # price
            buy.append(df_list[y].split("\n")[3]) # 거래일자
        elif df_list[y].split("\n")[2] != "빠른배송":
            size.append(df_list[y].split("\n")[0]) # size
            price.append(df_list[y].split("\n")[1]) # price
            buy.append(df_list[y].split("\n")[2]) # 거래일자

        
df = pd.DataFrame()

df["size"] = size
df["price"] = price
df["buy"] = buy

df
