import wikipediaapi
import urllib
import webbrowser
wiki_wiki = wikipediaapi.Wikipedia('pl')
a = input("Co mam znalezc? ")
page = wiki_wiki.page(a).fullurl
print(page)
webbrowser.open(page, new=2)