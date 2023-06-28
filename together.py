from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup
from lxml import etree
import requests

driver = webdriver.Chrome()
root_url = 'https://www.immoweb.be/en'

#cookies 
driver.get(root_url)
time.sleep(3)
element = driver.execute_script("""return document.querySelector('#usercentrics-root').shadowRoot.querySelector("button[data-testid='uc-accept-all-button']")""")
element.click()

'''#filtering urls list
site_model = etree.HTML(str(soup))
properties_per_page = site_model.xpath('//a[@class="card__title-link"]/@href')
#'//a[@class,"card__title-link"]'
#find_all('a', class_='card__title-link')
print(properties_per_page)
print("items on this page: ", len(properties_per_page))'''

urls = ['https://www.immoweb.be/en/classified/house/for-sale/braine%20l%27alleud/1420/10664357', 'https://www.immoweb.be/en/classified/apartment/for-sale/braine-l%27alleud/1420/10664356', 'https://www.immoweb.be/en/classified/house/for-sale/bouillon/6830/10339356', 'https://www.immoweb.be/en/classified/apartment/for-sale/saint-gilles/1060/10664355', 'https://www.immoweb.be/en/classified/house/for-sale/aalst/9300/10664353', 'https://www.immoweb.be/en/classified/house/for-sale/hofstade/9308/10664352', 'https://www.immoweb.be/en/classified/house/for-sale/arlon/6700/10664350', 'https://www.immoweb.be/en/classified/house/for-sale/virton/6760/10664349', 'https://www.immoweb.be/en/classified/house/for-sale/grivegn%C3%A9e/4030/10664348', 'https://www.immoweb.be/en/classified/house/for-sale/marche-en-famenne/6900/10664345', 'https://www.immoweb.be/en/classified/house/for-sale/genappe/1470/10664344', 'https://www.immoweb.be/en/classified/house/for-sale/waregem/8790/10664329', 'https://www.immoweb.be/en/classified/apartment/for-sale/waregem/8790/10664327', 'https://www.immoweb.be/en/classified/house/for-sale/genappe/1470/10664326', 'https://www.immoweb.be/en/classified/house/for-sale/sivry/6470/10621628', 'https://www.immoweb.be/en/classified/apartment/for-sale/waregem/8790/10664323', 'https://www.immoweb.be/en/classified/house/for-sale/schorisse/9688/10664322', 'https://www.immoweb.be/en/classified/house/for-sale/ronse/9600/10664321']

#getting main url
for url in urls:
    html_text = requests.get(url)
    soup = BeautifulSoup(html_text, 'html.parser')
    pretty = soup.prettify()

    #finding all the table of contants
    house = soup.find_all('tbody',class_='classified-table__body')
    interior_house = house[1].find_all('tr')
    facilities_house = house[3].find_all('tr')
    financial_house = house[6].find_all('tr')

    ''' Dictionary created in order to store the table headers (th) and their values (td)
A list is then creatted for each key and value to store the corresponding th and td
a for loop is then created to iterate over the multiple keys and values corresponding to the interior, whilst removing the trailing white spaces (strip)
'''
    interior={}
    interior_key=[]
    interior_value=[]

    for elem in interior_house:
        for th in elem.find_all('th'):
            print(th.contents[0].strip())
            interior_key.append(th.contents[0].strip())
            
        for td in elem.find_all('td'):
            print(td.contents[0].strip()) 
            interior_value.append(td.contents[0].strip())
        
    facilities={}
    facilities_key=[]
    facilities_value=[]

    for elem in facilities_house:
        for th in elem.find_all('th'):
            print(th.contents[0].strip())
            facilities_key.append(th.contents[0].strip())
            
        for td in elem.find_all('td'):
            print(td.contents[0].strip()) 
            facilities_value.append(td.contents[0].strip())
    ''' Looking at the 'td' tag, we see that there are 2 span tags with the list, conveying the same info. Hence, we only want the first value of the list.
    We look for all the spans and command that we print the first value'''
    ''' Looking at the 'td' tag, we see that there are 2 span tags with the list, conveying the same info. Hence, we only want the first value of the list.
    We look for all the spans and command that we print the first value'''
    financials={}
    financials_key=[]
    financials_value=[]

    for elem in financial_house:
        for th in elem.find_all('th'):
            print(th.contents[0].strip())
            financials_key.append(th.contents[0].strip())
            
        for td in elem.find_all('td'):
            if len(td.find_all('span'))>0:
                print(td.find_all('span')[0].contents[0].strip())
                financials_value.append(td.find_all('span')[0].contents[0].strip())
    ''' We only want to convey the price of the property. Therefore, once we have elements for the first key/value, add them to the dictionary  '''
    if financials_key and financials_value:
            financials[financials_key[0]] = financials_value[0]
            break






