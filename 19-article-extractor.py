# logic:
# make a request to the website that we are going be working with
# have the request processed in beautifulsoupe ----> parse it 
# find the part of the article that you want
# print the whole thing 
import requests
import sys
from bs4 import BeautifulSoup
page = requests.get('https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture')
soup = BeautifulSoup(page.content, 'html.parser')
article = soup.find(class_='grid--item body body__container article__body grid-layout__content')
def write_to_file(content):
    # a = print(article)
    f=open('/Users/xoempire/Desktop/Untitled.txt.rtf', 'w')
    f.write(f'{content}')
    f.close()
write_to_file(article)