import requests
from bs4 import BeautifulSoup
import time
from concurrent.futures import ThreadPoolExecutor
import pandas as pd
import re

#creating final list with all dict
skipped_urls = []
def needed(needed_things):
    list_of_needed = []
    list_of_needed.append(needed_things)
    print(needed_things)

def details_of_house(url):
    #assigning variables
    list_of_header = []
    list_of_data = []
    needed_things = {}
    things = ['Price', 'Address', 'Bedrooms',  'Energy class', 'Primary energy consumption','Furnished' ,'Terrace', 'Terrace surface', 'Surface of the plot', 'Living room surface', 'Number of frontages','Construction year', 'Building condition', 'Outdoor parking space', 'Bathrooms', 'Shower rooms', 'Office', 'Toilets', 'Kitchen type', 'Heating type',]
    
    try:
        #connecting to url
        html_text = requests.get(url)
        soup = BeautifulSoup(html_text.content, 'html.parser')

        #scraping data, header
        all_data = soup.find_all('td', class_='classified-table__data')
        all_header = soup.find_all('th', class_='classified-table__header')

        #getting text file of url
        text = soup.get_text()
        splited_text = text.split()

        #scrapping type of property, location, postal code, immocode from url
        str_url=str(url)
        split = str_url.split('/')
        for x in split:
            if x=='classified':
                needed_things['Type of property']=split[split.index(x)+1] 
                needed_things['Location'] = split[split.index(x)+3]
                needed_things['postal code'] = split[split.index(x)+4]
                needed_things['immo code'] = split[split.index(x)+5]

        for header in all_header:
            list_of_header.append(header.contents[0].strip())

        for data in all_data:
            list_of_data.append(data.contents[0].strip())

        #result_dict gives list_of_data and list_of_header in a dict format
        result_dict = {x: y for x, y in zip(list_of_header, list_of_data)}    

        #scraping price
        for word in splited_text:
            if word.startswith('€'):
                result_dict['Price'] = word.replace(',', '')

        #adding data needed in 'needed things'
        for element in things:
            if element in result_dict.keys():
                needed_things[element] = result_dict[element]
            else:
                needed_things[element] = 0

        needed(needed_things)
        return needed_things 
    
    except:
        print('error: skipped a line:' + url)
        skipped_urls.append(url)
        return None
    

#getting list of url from text file
with open("10k.txt", 'r') as input_file:  
        l = [line.rstrip() for line in input_file] 

        
House_details = []

#threading
with ThreadPoolExecutor(max_workers=10) as executor:
        start = time.time()
        futures = [executor.submit(details_of_house, url) for url in l]
        House_details = [item.result() for item in futures if item.result() is not None]
        end = time.time()
        print('House_details',House_details)
        print("Time Taken: {:.6f}s".format(end - start))
        print("skipped urls: ", skipped_urls)

#creating csv
df = pd.DataFrame(House_details)
df.to_csv('scraped_data_10.csv', index=False)

#collecting skipped url 
with open('skipped.txt', 'a') as output_file:
    for line in skipped_urls:
        output_file.write(f"{line}\n")