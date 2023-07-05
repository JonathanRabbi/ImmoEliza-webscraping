#import utils.get_urls as get_urls
from bs4 import BeautifulSoup
from lxml import etree
import requests
import json

base_url = 'https://www.immoweb.be/en/search/house-and-apartment/for-sale?countries=BE&postalCodes=BE-4920,4910&orderBy=newest&page='     #4910 & 4920 to have 5 result pages, 112 results
page_url = base_url

html_text= requests.get(base_url).text 
soup = BeautifulSoup(html_text, 'html.parser')
site_model = etree.HTML(str(soup))
properties_per_page = site_model.xpath('//main/div//a[@class="card__title-link"]/@href') #creates a list of all search results (and excludes "similar properties" and "sponsored properties" )
print(properties_per_page)

print("items on this page: ", len(properties_per_page))
unique_properties_per_page = list(set(properties_per_page)) #create a list of unique properties by creating a set and turning that into a list again
print(unique_properties_per_page)
print("items on this page: ", len(unique_properties_per_page))

"""Get the number of pages"""
list_of_pages = site_model.xpath('//*[@id="searchResults"]/div[3]/div/div[1]/div[1]/div[1]/div/div[1]/div/nav/ul/li[-1]')
print(list_of_pages)

for i in range (1,6):
    page_url = base_url + str(i)
    print(page_url)

    """ignore this section"""
"""with open('20k_belgium_url_list.txt', 'r') as input_file:
    list2check = input_file.readlines()

print(list2check)"""

with ThreadPoolExecutor(max_workers=10) as executor:
    start = time.time()
    futures = [executor.submit(house_scrapper, url) for url in url_list]
    results =  [item.result() for item in futures]
    end = time.time()
    print("Time Taken: {:.6f}s".format(end-start))
    print(results)