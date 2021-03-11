# logic:
# the program woudl extract the content of an article from a webpage
# the content of the article would be stred in a file
# s file woudl be opened in the write mode
# the article woudl be written to the fule
# the file woudl be closed
import requests
import sys
from bs4 import BeautifulSoup
page = requests.get('https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture')
soup = BeautifulSoup(page.content, 'html.parser')
article = soup.find(class_='grid--item body body__container article__body grid-layout__content')
def write_to_file(content):
    # a = print(article)
    f=open('/Users/xoempire/Desktop/Untitled.txt.rtf', 'w')
    f.writelines(f'{content}')
    f.close()
    f=open('/Users/xoempire/Desktop/Untitled.txt.rtf')
    contenty=f.read()
    print(contenty)
write_to_file(article)