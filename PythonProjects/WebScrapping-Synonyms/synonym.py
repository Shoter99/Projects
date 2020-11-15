import requests
from bs4 import BeautifulSoup as bs
synonim = input("Podaj wyraz: ")
URL = 'https://www.synonimy.pl/synonim/ciekawy/'
page = requests.get(URL)
print(page)
soup = bs(page.content, 'html.parser')
result = soup.find(id='word_load')
print(result)
synonyms = result.find_all('dd', class_='term')
for synonym in synonyms:
    print(synonym, end='/n'*2)
