## 개별 상품 URL 수집

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
##############################
#240부터일때  
#driver.find_element_by_xpath('//*[@id="__layout"]/div/div[2]/div[1]/div/div[2]/div/div[6]/div/div[2]/div[1]/div[2]/div/div/div/div/div[2]/ul/li[8]/a').click()

#230부터일때
#driver.find_element_by_xpath('//*[@id="__layout"]/div/div[2]/div[1]/div/div[2]/div/div[6]/div/div[2]/div[1]/div[2]/div/div/div/div/div[2]/ul/li[12]/a').click()

#220
#driver.find_element_by_xpath('//*[@id="__layout"]/div/div[2]/div[1]/div/div[2]/div/div[6]/div/div[2]/div[1]/div[2]/div/div/div/div/div[2]/ul/li[12]/a').click()

#215
driver.find_element_by_xpath('//*[@id="__layout"]/div/div[2]/div[1]/div/div[2]/div/div[6]/div/div[2]/div[1]/div[2]/div/div/div/div/div[2]/ul/li[13]/a').click()

##############################

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
