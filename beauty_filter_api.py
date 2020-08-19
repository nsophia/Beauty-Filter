from selenium import webdriver
import time
import sys
from bs4 import BeautifulSoup

# Opens Chrome browser in incognito mode 
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--headless')
driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver", chrome_options=options)
url = 'https://www.ulta.com/all-nighter-ultra-glow-makeup-setting-spray?productId=pimprod2017480'
driver.get(url)

# Opens the ingredients list 
ingr_buttons = driver.find_elements_by_class_name("ProductDetail_ingredients")
driver.execute_script('arguments[0].click();', ingr_buttons)
time.sleep(1)

page_source = driver.page_source

# Use BeautifulSoup to 
soup = BeautifulSoup(page_source, 'lxml')
ingred = []



