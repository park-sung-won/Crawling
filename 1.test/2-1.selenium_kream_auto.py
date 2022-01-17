# Kream 카테고리 검색결과 자동화

options = webdriver.ChromeOptions() ## 웹사이트 띄우지 않고 수집하기
options.add_argument("headless")
driver = webdriver.Chrome("./chromedriver", options=options)
driver.get("https://kream.co.kr/search?category_id=1&tag_id[gender]=45&tag_id[sneakers_size]=97&keyword=Dunk%20low&sort=popular&per_page=40") # URL 

driver.find_element_by_xpath('//*[@id="__layout"]/div/div[1]/div[1]/div/ul/li[4]/a').click()

time.sleep(0.5)

# 로그인 아이디/비밀번호
login = driver.find_element_by_xpath('//*[@id="__layout"]/div/div[2]/div[1]/div/div[1]/div/input')
login.send_keys("ID")

password = driver.find_element_by_xpath('//*[@id="__layout"]/div/div[2]/div[1]/div/div[2]/div/input')
password.send_keys("PASSWORD")

time.sleep(0.5)
driver.find_element_by_css_selector(".btn.full.solid").click()

# 검색결과 페이지 결과리스트 스크롤 
for c in range(0,10):
    driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)
    time.sleep(2)

# for w in range(5):                                                      # 스크롤 횟수 지정 = range(횟수)
#     try:
#         driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # 스크롤 명령 
#         print('스크롤 횟수 : ', (w+1))                                                     # 몇번째 스크롤되고 있는지 확인
#     except:
#         pass
#     time.sleep(2.5) 

time.sleep(3)

for i in trange(41,50):   # item 넘버 > 범위 지정 range(a,b)
    time.sleep(3)
    driver.find_element_by_xpath(f'//*[@id="__layout"]/div/div[2]/div[5]/div/div[3]/div[1]/div[{i}]').click()

    item = driver.find_element_by_xpath(f'//*[@id="__layout"]/div/div[2]/div[5]/div/div[3]/div[1]/div[{i}]/a/div[2]/div[1]/p[2]').text
    
    time.sleep(2)
    driver.find_element_by_css_selector(".btn.outlinegrey.full.medium").click()

    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="panel1"]/div/div/div[1]/div/div[3]/a/span').click()
    time.sleep(2)

    scr1 = driver.find_element_by_xpath('//*[@id="panel1"]/div/div/div[2]')  # 스크롤할 영역지정
    for x in range(50):                                                      # 스크롤 횟수 지정 = range(횟수)
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

    df.to_csv(f"./{i}_{item}")
    print(df)
    driver.back()
    time.sleep(3)

