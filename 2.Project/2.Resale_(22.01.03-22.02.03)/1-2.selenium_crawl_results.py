## 전체 상품 검색리스트 개별 거래데이터 수집

options = webdriver.ChromeOptions()
options.add_argument("headless")
driver = webdriver.Chrome("./chromedriver", options=options)
driver.get("https://kream.co.kr/search?category_id=1&tag_id[sneakers_size]=97&tag_id[gender]=45&keyword=Jordan%201%20low&sort=popular&per_page=40")

driver.find_element_by_xpath('//*[@id="__layout"]/div/div[1]/div[1]/div/ul/li[4]/a').click()

time.sleep(0.5)

login = driver.find_element_by_xpath('//*[@id="__layout"]/div/div[2]/div[1]/div/div[1]/div/input')
login.send_keys("ID")

password = driver.find_element_by_xpath('//*[@id="__layout"]/div/div[2]/div[1]/div/div[2]/div/input')
password.send_keys("PASSWORD!")

time.sleep(1)
driver.find_element_by_css_selector(".btn.full.solid").click() #로그인 완료
#########

time.sleep(3)

for i in trange(1,41):   # item 넘버
#     time.sleep(5) # 상품선택
    item_inner = driver.find_element_by_xpath(f'//*[@id="__layout"]/div/div[2]/div[5]/div[2]/div[3]/div[1]/div[{i}]/a').click()
    
    #item_inner = driver.find_element_by_class_name('item_inner')
    driver.switch_to.frame(item_inner)
    
    time.sleep(3)
    item_detail = driver.find_element_by_xpath('//*[@id="__layout"]/div/div[2]/div[1]/div/div[2]/div/div[2]/div').text
    print(item_detail)
    
    item = driver.find_element_by_xpath('//*[@id="__layout"]/div/div[2]/div[1]/div/div[2]/div/div[1]/div[1]/div/p[1]').text
    print(item)
    time.sleep(2)
    driver.find_element_by_css_selector(".btn.outlinegrey.full.medium").click()

    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="panel1"]/div/div/div[1]/div/div[3]/a/span').click()
    time.sleep(2)
    
    time.sleep(4)
    print(i,':', driver.find_element_by_xpath('//*[@id="__layout"]/div/div[2]/div[1]/div/div[2]/div/div[2]/div/dl').text)
    
    scr1 = driver.find_element_by_xpath('//*[@id="panel1"]/div/div/div[2]')  # 스크롤할 영역지정
    for x in range(0):                                                      # 스크롤 횟수 지정 = range(횟수)
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

    df.to_csv(f"./JD/{i}_{item}")     ###### 파일경로 확인하기 ######
    print(df)
    driver.back()
    time.sleep(3)

#    driver.find_element_by_id("div")
    
#driver.switch_to.frame(iframe)    
#//*[@id="__layout"]/div/div[2]/div[5]/div[2]/div[3]/div[1]/div[{i}]/a
#//*[@id="__layout"]/div/div[2]/div[5]/div[2]/div[3]/div[1]/div[2]/a

# time.sleep(4) # 상품선택
# driver.find_element_by_xpath(f'//*[@id="__layout"]/div/div[2]/div[5]/div[2]/div[3]/div[1]/div[1]').click()
#driver.find_element_by_class_name('item_inner')

# #driver.find_element_by_xpath(f'//*[@id="__layout"]/div/div[2]/div[5]/div[2]/div[3]/div[1]/div[{1}]').click()
