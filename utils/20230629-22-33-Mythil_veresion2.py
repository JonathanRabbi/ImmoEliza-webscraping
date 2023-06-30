import requests
from bs4 import BeautifulSoup
import time
from concurrent.futures import ThreadPoolExecutor
import pandas as pd
import re

def needed(needed_things):
    list_of_needed = []
    list_of_needed.append(needed_things)
    print(needed_things)

def details_of_house(url):
    list_of_header = []
    list_of_data = []
    things = ['Price', 'Address', 'Locality', 'Bedrooms',  'Energy class', 'Primary energy consumption','Furnished' ,'Terrace', 'Terrace surface', 'Surface of the plot', 'Living room surface', 'Number of frontages','Construction year', 'Building condition', 'Outdoor parking space', 'Bathrooms', 'Shower rooms', 'Office', 'Toilets', 'Kitchen type', 'Heating type',]
    
    
    html_text = requests.get(url)
    soup = BeautifulSoup(html_text.content, 'html.parser')

    text = soup.get_text()
    splited_text = text.split()
   
    all_data = soup.find_all('td', class_='classified-table__data')
    all_header = soup.find_all('th', class_='classified-table__header')
    immoweb_code_text = soup.find(class_='classified__header--immoweb-code').text.strip()
    immo_code = re.findall('([0-9]+)', immoweb_code_text)
    
    for header in all_header:
        list_of_header.append(header.contents[0].strip())

    for data in all_data:
        list_of_data.append(data.contents[0].strip())

    result_dict = {x: y for x, y in zip(list_of_header, list_of_data)}

    for word in splited_text:
        if word.startswith('€'):
            result_dict['Price'] = word.replace(',', '')    
    
    needed_things = {}
    for element in things:
        if element in result_dict.keys():
            needed_things[element] = result_dict[element]
        else:
            needed_things[element] = 0
    
    needed_things['immo_code'] = immo_code
    
    needed(needed_things)
    
    return needed_things

"""with open("sliceover10k.txt", 'r') as input_file:   #source file for scraping
    l = [line.rstrip() for line in input_file]      #check list name """
l = [
    'https://www.immoweb.be/en/classified/apartment/for-sale/jambes/5100/10667600',
    'https://www.immoweb.be/en/classified/house/for-sale/fontaine-l%27ev%C3%AAque/6140/10667595',
    'https://www.immoweb.be/en/classified/house/for-sale/neuville-en-condroz/4121/10667592']

results = []

with ThreadPoolExecutor(max_workers=10) as executor:
        start = time.time()
        futures = [executor.submit(details_of_house, url) for url in l]
        results = [item.result() for item in futures]
        end = time.time()
        print(results)
        print("Time Taken: {:.6f}s".format(end - start))

df = pd.DataFrame(results)
creator = "DeFre"    #change creator to name of creator to ensure unique filename
timestamp = time.strftime("%Y%m%d-%H%M%S") #add date and time of creation
output_path = "data/"      #leave empty to save the file in the same folder as your code, 
output_filename = output_path + "scraped_data_" + creator + timestamp + ".csv" #assemble filename
df.to_csv(output_filename, index=False)
