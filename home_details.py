import requests
from bs4 import BeautifulSoup



#root_url = 'https://www.immoweb.be/en'
list_of_urls = ['https://www.immoweb.be/en/classified/house/for-sale/aywaille/4920/10600649', 'https://www.immoweb.be/en/classified/house/for-sale/lede/9340/10660142']

result_dict = {}  # Initialize an empty dictionary

def home_scrape(lis_of_urls):
    result_list=[]
    for url in list_of_urls:
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

        result_dict=({x:y for x, y in zip(list_of_header, list_of_data)})
        result_list.append(result_dict)

        return result_list

results = home_scrape(list_of_urls)
for result in results:
    print(result)






