import requests
from bs4 import BeautifulSoup as bs
synonim = input("Podaj wyraz: ")
URL = 'https://www.synonimy.pl/synonim/ciekawy/'
page = requests.get(URL)
print(page)
soup = bs(page.content, 'html.parser')
print(soup.dl)
