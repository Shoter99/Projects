encoding = 'utf-8'
import webbrowser
import wikipedia as wi
wi.set_lang('pl')
haslo = input("Co mam znalezc?")

wynik = wi.page(haslo)

print(wynik.title)
print(wynik.url)
webbrowser.open(wynik.url)
input()