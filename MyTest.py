import requests 
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup
import requests

for_sale = '/search/house/for-sale'
for_rent = '/search/house/for-rent' 

list_of_districts = ['/brussels' ] #, '/wallonia', '/gent', '/namur', '/hainaut', '/liege , '/antwerp''
end_url= '/district?countries=BE&page=1&orderBy=relevance'
root_url = 'https://www.immoweb.be/en'

cookie_url = root_url + '/cookie'

session = requests.Session()
cookies = session.cookies
driver = webdriver.Chrome()

driver.get(root_url+'/shadow_dom.html')
time.sleep(3)
element = driver.execute_script("""return document.querySelector('#usercentrics-root').shadowRoot.querySelector("button[data-testid='uc-accept-all-button']")""")
element.click()

for i in range(len(list_of_districts)):
    current_link = root_url+for_rent+list_of_districts[i]+end_url
    driver.get(current_link)
    time.sleep(3)

    print(current_link)

    search_results = driver.find_elements(By.CLASS_NAME, "search-results__item")
    time.sleep(3)
    for result in search_results:
        result.click()
        time.sleep(3)
        
        table = driver.find_elements(By.CLASS_NAME, 'classified-table__row' )
        for x in table:
            print(x.text)
driver.close() 