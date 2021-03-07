# logic:
# making a request to the webpage
# craete a beautifulsoup object from the page and parse it
# from the objet call all the tags which contain links
# get the content of all the links
# print all the links in seperate lines

import requests
import re
from bs4 import BeautifulSoup
domain=input('enter the name of the domain: ')
page=requests.get(domain)
soupe = BeautifulSoup(page.content, 'html.parser')
link_tags=soupe.find_all('link')
for i in link_tags:
    b=i.get('href')
    print(f'{b}\n')

