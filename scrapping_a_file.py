import requests 
from bs4 import BeautifulSoup
import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

for_sale = '/search/house/for-sale'
for_rent = '/search/house/for-rent' 

list_of_districts = ['/brussels' ] #, '/wallonia', '/gent', '/namur', '/hainaut', '/liege , '/antwerp''
end_url= '/district?countries=BE&page=1&orderBy=relevance'

root_url = 'https://www.immoweb.be/en'
for i in range(len(list_of_districts)):
    current_url = root_url+for_rent+list_of_districts[i]+end_url
    print(current_url)

    driver = webdriver.Chrome()
    driver.get(current_url)
    time.sleep(10)

    search_results = driver.find_elements(By.CLASS_NAME, "search-results__item")

    for result in search_results:
       result.click()
       
       #print(result.text)



