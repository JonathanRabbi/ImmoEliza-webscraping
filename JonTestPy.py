from bs4 import BeautifulSoup
import requests

#html_text= requests.get('https://www.immoweb.be/en/classified/exceptional-property/for-sale/antwerp/2000/10591004').text

html_text= requests.get('https://www.immoweb.be/en/search/house/for-sale/east-flanders/province?countries=BE&page=1&orderBy=relevance').text
#print(html_text)

soup = BeautifulSoup(html_text, 'html.parser')
#print(soup.prettify())

Body_overview = soup.xpath('//head')
#'//a[@class,"card__title-link"]'
#find_all('a', class_='card__title-link')
print(Body_overview)

"""Body_overview= soup.find_all('a', class_='card__title-link')
print(Body_overview)"""
