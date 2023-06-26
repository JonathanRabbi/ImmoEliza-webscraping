from bs4 import BeautifulSoup
import re
import requests
import json

root_url = 'https://www.immoweb.be/en'

session=requests.Session()
a = session.get(root_url)


