import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

options = Options()
# options.add_argument('--headless')
# options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


driver.get('')

time.sleep(4)
search = driver.find_element(By.CLASS_NAME,"index-search-input")
search.send_keys("7707049388")
search.send_keys(Keys.RETURN)

time.sleep(5)

content = driver.page_source
page = BeautifulSoup(content, "html.parser")

result = page.find_all('dd',itemprop="foundingDate")

print(result[0].get_text())
driver.close()
