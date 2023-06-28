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