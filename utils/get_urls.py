"""This file contains all functions related to the gathering of urls for sitescraping"""

from bs4 import BeautifulSoup
from lxml import etree
import requests

# Variables
###########

# html_text= requests.get('https://www.immoweb.be/en/classified/exceptional-property/for-sale/antwerp/2000/10591004').text  #property result used as example by Jonathan
# "https://www.immoweb.be/en/search/house-and-apartment/for-sale?countries=BE&orderBy=newest&page=1" #starting point for all housing properties of Belgium, sorted starting from newest
# "https://www.immoweb.be/en/search/house-and-apartment/for-sale/Theux/4910?countries=BE&page=1&orderBy=newest"   #4910 to have a pool of (47) but some oddball properties like castle, farmhouse and duplex
base_url = 'https://www.immoweb.be/en/search/house-and-apartment/for-sale?countries=BE&postalCodes=BE-4920,4910&orderBy=newest&page='     #4910 & 4920 to have 5 result pages, 112 results
page_url = base_url #will get a page NUMBER attached later, but this way page_url can be called already, immoweb does not mind the missing page number


def get_model(page_url): 
    """Turn the url into a nice soup and use etree to get a model which xpath understands"""
    html_text= requests.get(page_url).text 
    #print(html_text)
    soup = BeautifulSoup(html_text, 'html.parser') 
    site_model = etree.HTML(str(soup))

def get_property_list():
    """extract the urls of all search results from the page"""
    properties_per_page = site_model.xpath('//main/div//a[@class="card__title-link"]/@href') #creates a list of all search results (and excludes "similar properties" and "sponsored properties" )
    print(properties_per_page)
    print("items on this page: ", len(properties_per_page))
    unique_properties_per_page = list(set(properties_per_page)) #create a list of unique properties by creating a set and turning that into a list again
    print(unique_properties_per_page)
    print("items on this page: ", len(unique_properties_per_page))

def run_through_pages():
    for i in range (1,6):
    page_url = base_url + str(i)
    print(page_url)

def page_list_to_full_list
