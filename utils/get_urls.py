"""This file contains all functions related to the gathering of urls for sitescraping"""

from bs4 import BeautifulSoup
from lxml import etree
import requests
from random import randint
import time
from time import sleep
import json

# Variables
###########

# html_text= requests.get('https://www.immoweb.be/en/classified/exceptional-property/for-sale/antwerp/2000/10591004').text  #property result used as example by Jonathan
base_url = "https://www.immoweb.be/en/search/house-and-apartment/for-sale?countries=BE&orderBy=newest&page=" #starting point for all housing properties of Belgium, sorted starting from newest
# "https://www.immoweb.be/en/search/house-and-apartment/for-sale/Theux/4910?countries=BE&page=1&orderBy=newest"   #4910 to have a pool of (47) but some oddball properties like castle, farmhouse and duplex
# base_url = 'https://www.immoweb.be/en/search/house-and-apartment/for-sale?countries=BE&postalCodes=BE-4920,4910,4000&orderBy=newest&page='     #4910 & 4920 to have 5 result pages, 112 results
page_url = base_url #will get a page NUMBER attached later, but this way page_url can be called already, immoweb does not mind the missing page number


def get_model(page_url): 
    """Turn the url into a nice soup and use etree to get a model which xpath understands"""
    print(page_url)
    html_text= requests.get(page_url).text 
    #print(html_text)
    soup = BeautifulSoup(html_text, 'html.parser') 
    site_model = etree.HTML(str(soup))
    return site_model


def get_property_list(site_model):
    """extract the urls of all search results from the page"""
    properties_per_page = site_model.xpath('//main/div//a[@class="card__title-link"]/@href') #creates a list of all search results (and excludes "similar properties" and "sponsored properties" )
    #print(properties_per_page)
    #print("items on this page: ", len(properties_per_page))
    """unique_properties_per_page = list(set(properties_per_page)) #create a list of unique properties by creating a set and turning that into a list again
    print(unique_properties_per_page)
    print("items on this page: ", len(unique_properties_per_page))
    properties_per_page = unique_properties_per_page"""
    return properties_per_page

def page_list_to_full_list(full_list, properties_per_page):
    """adds urls to the full list of urls"""
    #print(full_list)
    #print(type(unique_properties_per_page))
    full_list.extend(properties_per_page)
    #print(full_list)
    print("list length: ",len(full_list))
    return full_list

"""def add_to_file(properties_per_page):
    with open('20k_belgium_url_list.json', 'a') as output_file:
        json.dump(properties_per_page, output_file)"""

def add_to_file(properties_per_page):
    with open('20230630_url_list.txt', 'a') as output_file:
        for line in properties_per_page:
            output_file.write(f"{line}\n")


def run_through_pages():
    """Scrapes property urls from search results page after page"""
    full_list = []
    for i in range (1,333):
        sleep(randint(1,3))
        page_url = base_url + str(i)
        site_model = get_model(page_url)
        properties_per_page = get_property_list(site_model)
        #print(full_list)
        full_list = page_list_to_full_list(full_list, properties_per_page)
        add_to_file(properties_per_page)
        print(i)
    return full_list


start = time.time()
final_list = run_through_pages()
#print("final list:", final_list)
#print("final list length: ",len(final_list))
end = time.time()
print("Time Taken: {:.6f}s".format(end-start))
