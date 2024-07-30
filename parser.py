from flask import Flask
from flask import request
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import requests

#You need to use following line [app Flask(__name__]
app = Flask(__name__)
@app.route('/')
def index():
    return "Hello World with flask"


@app.route("/data")
def data():
    id_contact = request.args.get('id', '')
    inn = request.args.get('inn', '')
    options = Options()
# options.add_argument('--headless')
# options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


    driver.get('')
    time.sleep(30)
    search = driver.find_element(By.CLASS_NAME,"index-search-input")
    search.send_keys(str(inn))
    search.send_keys(Keys.RETURN)

    time.sleep(19)

    content = driver.page_source
    page = BeautifulSoup(content, "html.parser")

    result = page.find_all('dd',itemprop="foundingDate")

    print(result[0].get_text())


    driver.get(f'/crm.company.update?id={id_contact}&fields[UF_CRM_1722263448032]={result}')
    time.sleep(1)
    driver.close()

    return id_contact + inn    

if __name__ == '__main__':
    app.run(port=5000,debug=True)
