import requests
from bs4 import BeautifulSoup
import time
from concurrent.futures import ThreadPoolExecutor
import pandas as pd



def needed(needed_things):
    list_of_needed = []
    list_of_needed.append(needed_things)
    print(needed_things)


def details_of_house(url):

    list_of_header = []
    list_of_data = []
    
    things  = ['Price', 'Address', 'Locality', 'Bedrooms',  'Energy class', 'Primary energy consumption',  'Kitchen type',  'Furnished' ,'Terrace', 'Terrace surface', 'Surface of the plot', 'Living room surface', 'Number of frontages']
    
    #connecting url with soup
    html_text = requests.get(url)
    soup = BeautifulSoup(html_text.content, 'html.parser')

    #converting html file into text
    text = soup.get_text()
    splited_text=text.split()
   
    #collecting data
    all_data = soup.find_all('td' , class_ = 'classified-table__data')
    all_header = soup.find_all('th', class_='classified-table__header')
    immoweb_code_text = soup.find(class_='classified__header--immoweb-code').text.strip()
    immo_code = re.findall('([0-9]+)',immoweb_code_text)#scraping immo code with regex

    for header in all_header:
        list_of_header.append(header.contents[0].strip())

    for data in all_data:
        list_of_data.append(data.contents[0].strip())

    #creating dict with details of house
    result_dict = { x:y for x,y in zip(list_of_header, list_of_data)}

    #scraping price
    for word in splited_text:
        if word.startswith('€'):
            result_dict['Price'] = word.replace(',', '')    
    
    #filtering needed details from result_dict
    needed_things={}
    for element in things:
        if element in result_dict.keys():
            needed_things[element]=result_dict[element]
        else:
            needed_things[element]=0
    
        needed_things['immo_code']=immo_code # adding immo_code to needed things
      
    needed(needed_things) 

    l =['https://www.immoweb.be/en/classified/apartment/for-sale/jambes/5100/10667600','https://www.immoweb.be/en/classified/house/for-sale/fontaine-l%27ev%C3%AAque/6140/10667595','https://www.immoweb.be/en/classified/house/for-sale/neuville-en-condroz/4121/10667592']
    for x in l:
        details_of_house(x)
    
    with ThreadPoolExecutor(max_workers=10) as executor:
        start = time.time()
        futures = [executor.submit(details_of_house, url) for url in l]
        results = [item.result() for item in futures]
        end = time.time()
        print("Time Taken: {:.6f}s".format(end - start))
        print(results)

    df=pd.DataFrame(results)
    df.to_csv('scraped_data.csv', index=False)
