## 상품 정보(텍스트) 수집하기

options = webdriver.ChromeOptions()
options.add_argument("headless")
driver = webdriver.Chrome("./chromedriver", options=options)
driver.get("https://kream.co.kr/search?category_id=1&tag_id[gender]=45&tag_id[sneakers_size]=97&keyword=jordan%201%20low&sort=popular&per_page=40")


time.sleep(3)

p_name = []
p_num = []
p_day = []
p_col = []
p_price = []
p_wish = []

for i in trange(1,41):   # item 넘버
    time.sleep(2)
    driver.find_element_by_xpath(f'//*[@id="__layout"]/div/div[2]/div[5]/div/div[3]/div[1]/div[{i}]').click()

    time.sleep(3)
    
    html = driver.page_source
    soup = bs(html, "html.parser")
    name = soup.findAll('p', attrs={'class': 'title'})
    tags = soup.findAll('div', attrs={'class': 'detail_box'})
    wish = soup.findAll('span', attrs={'class': 'wish_count_num'})

    p_name.append(str(name[0]).split(">")[1].split("<")[0])
    p_num.append(str(tags[0]).split(">")[4].split("<")[0])
    p_day.append(str(tags[1]).split(">")[4].split("<")[0])
    p_col.append(str(tags[2]).split(">")[4].split("<")[0])
    p_price.append(str(tags[3]).split(">")[4].split("<")[0])
    p_wish.append(str(wish[0]).split(">")[1].split("<")[0])

    time.sleep(2)
  
    driver.back()
    time.sleep(3)
    
df = pd.DataFrame()

df["name"] = p_name
df["num"] = p_num
df["day"] = p_day
df["col"] = p_col
df["price"] = p_price
df["wish"] = p_wish

df.to_csv("text_jordan_1_low.csv", index = False)
pd.read_csv("text_jordan_1_low.csv")
