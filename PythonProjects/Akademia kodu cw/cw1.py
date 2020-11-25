import random as rand
"""
print("Jestem Super")


x = input("Wyraz")
print("Hello "+x)

goscie = input("Ilu będzie gości? ")
cukierki = input("Ile masz cukierków? ")
pozostale = int(cukierki) % int(goscie)
po_ile = (int(cukierki)-pozostale)/int(goscie)
print("Zostanie Ci %d" % pozostale)
print("Goście dostaną po %d " % po_ile)

for i in range(0, 20):
    print("*", end="")

liczba = input("\nPodaj liczbe")
print(len(liczba))

try:
    liczba = int(liczba)
    print(liczba*10)
except:
    print("Nie podano liczby")

wyraz = input("Podaj wyraz: ")
print(wyraz[0])

losowa = rand.randrange(1, 6)
print(losowa)

wiek = int(input("Podaj swój wiek: "))
if wiek > 13 and wiek < 17:
    print("Jesteś nastolatkiem")
else:
    print("Nie jesteś nastolatkiem")

godzina = input("która jest godzina: ")
if godzina == 9 or godzina == 12:
    print("Masz wypić kawę")

for i in range(1, 6):
    print(i*"*")

napis = input("Wpisz wyraz: ")

if "kot" in napis:
    print(True)
else:
    print(False)

dane = input("Wpisz nazwe z wielkich liter: ")

print(dane.lower())

akademia = input("Wpisz akademia: ")

if akademia == "Akademia":
    print(True)

print("1 3 5 ? 9")
print("2 4 6 ? 10")
odp = ""
while odp != "7 2":
    odp = input("Co trzeba wstawić pod znakiem zapytania? ")
    if odp == "7 2":
        print("Dobrze")
    else:
        print("nie udało sie")

znajomi = ['znaj1', 'znaj2', 'znaj3', 'znaj4']
print(rand.choice(znajomi))

litera = input('Podaj jakis wyraz zaczynajacy sie na "a"')
if litera[0].lower() == 'a':
    print(True)
else:
    print(False)

dwa = input('Podaj dwa wyrazy: ')
try:

    dwa = dwa.split(sep=" ")
    if dwa[0] == dwa[1]:
        print(True)
    elif dwa[2] != "":
        print('Podano więcej wyrazów')
    else:
        print(False)
except:
    print('Nie podano dwóch wyrazów')



def check(x):
    return x[::-1]


palidrom = ""
while palidrom == "":
    palidrom = input("Podaj jakiś palidrom: ")

    if palidrom == "":
        print("nie podano wyrazu")
    else:
        if palidrom == check(palidrom):
            print("tak")
        else:
            print("nie")

liczba = input("Podaj dwie liczby: ")
try:
    l1, l2 = liczba.split(sep=" ")
    print(int(l1)**int(l2))
except:
    print("Nie podano dwóch liczb")

ciag = input("Wpisz wyraz: ")
print(ciag.replace("*", ""))

w = input("Wpisz wyraz: ")
if w[-3:] == 'tka':
    print(True)
else:
    print(False)
"""
