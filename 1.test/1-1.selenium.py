# 셀레니움 활용 어스2 키워드 검색 진입
# 어스2 URL : https://app.earth2.io/#thegrid

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome("./chromedriver")
driver.get("https://app.earth2.io/#thegrid")

driver.find_element_by_css_selector(".styles_modalBtn__JRS92.styles_modalCloseBtn__2GqKd").click()

time.sleep(1)
elem_search = driver.find_element_by_class_name("mapboxgl-ctrl-geocoder--input")
elem_search.send_keys("서울")

time.sleep(1)
elem_search.send_keys(Keys.RETURN)
