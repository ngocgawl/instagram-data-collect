#import xml.etree.ElementTree as ET
# import requests as req
# from requests_html import HTMLSession
# from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driverManager = ChromeDriverManager()
driver = webdriver.Chrome(service=Service(driverManager.install()))
driver.implicitly_wait(10)

url = 'https://www.instagram.com/p/CcGhM6zofoZ/'
driver.get(url)

driver.find_element(By.CSS_SELECTOR, '[name="username"]').send_keys("ngoc@gawl.eu")
driver.find_element(By.CSS_SELECTOR, '[name="password"]').send_keys("gslnhung")
driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()

article = driver.find_element(By.TAG_NAME, 'article')
print(article.text)


# session = HTMLSession()
# res = session.get(url)
# res.html.render()

# html_text = res.html.html
# soup = BeautifulSoup(html_text, 'lxml')

# article_txt = soup.find_all('a')
# print(article_txt)

# soup_article = BeautifulSoup(article_txt, 'html.parser')
# header_txt = soup_article.find('header').text

# soup_header = BeautifulSoup(header_txt, 'html.parser')
# user = soup_header.find('a').text
# print(user)

# for link in soup.find_all('a'):
#     print(link.get('href'))