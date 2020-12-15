from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#URL = 'https://www.ulta.com/all-nighter-ultra-glow-makeup-setting-spray?productId=pimprod2017480'
# ProductDetail_productContent
URL = 'https://www.ulta.com/child-eyeshadow-palette?productId=pimprod2021201'
driver = webdriver.Firefox(executable_path='/home/sophia/geckodriver')

driver.get(URL)
time.sleep(2)

#driver.findElement(By.css("div.liCollapsed")).click()
driver.find_element_by_css_selector(".MixedMenuButton").click()

links = driver.find_elements_by_xpath("//div[@class='collapsableContent empty']/preceding-sibling::div[@class='collapsableHeader']")







