import requests
from bs4 import BeautifulSoup
import time
from concurrent.futures import ThreadPoolExecutor
import pandas as pd

list_urls = ['https://www.immoweb.be/en/classified/house/for-sale/aywaille%20sougn%C3%A9-remouchamps/4920/10663667', 'https://www.immoweb.be/en/classified/villa/for-sale/aywaille/4920/10661605', 'https://www.immoweb.be/en/classified/villa/for-sale/aywaille/4920/10660061', 'https://www.immoweb.be/en/classified/house/for-sale/aywaille/4920/10660060', 'https://www.immoweb.be/en/classified/apartment/for-sale/jambes/5100/10667600']
things = ['Price', 'Address', 'Locality', 'Bedrooms',  'Energy class', 'Primary energy consumption','Furnished' ,'Terrace', 'Terrace surface', 'Surface of the plot', 'Living room surface', 'Number of frontages','Construction year', 'Building condition', 'Outdoor parking space', 'Bathrooms', 'Shower rooms', 'Office', 'Toilets', 'Kitchen type', 'Heating type',]
list_of_needed = []


def home_scrape(url):
    result_dict = {}

    html_text = requests.get(url)
    soup = BeautifulSoup(html_text.content, 'html.parser')

    all_data = soup.find_all('td', class_='classified-table__data')
    all_header = soup.find_all('th', class_='classified-table__header')

    list_of_header = []
    list_of_data = []
    for header in all_header:
        list_of_header.append(header.contents[0].strip())
    for data in all_data:
        if len(data.find_all('span')) > 0:
            span_content = data.find_all('span')[0].contents[0].strip()
            list_of_data.append(span_content)
        else:
            list_of_data.append(data.contents[0].strip())

    result_dict = {x:y for x, y in zip(list_of_header, list_of_data)}

    needed_things = {}
    for x in things:
        if x in result_dict.keys():
            needed_things[x] = result_dict[x]
        else:
            needed_things[x] = 0
    return needed_things
    
with ThreadPoolExecutor(max_workers=10) as executor:
    start = time.time()
    futures = [executor.submit(home_scrape, url) for url in list_urls]
    results = [item.result() for item in futures]
    end = time.time()
    print("Time Taken: {:.6f}s".format(end - start))
    print(results)

df=pd.DataFrame(results)
df.to_csv('scraped_data.csv', index=False)
