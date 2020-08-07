import random as rand
import time

x = rand.randint(0,8)
hasla = ["miasto", "rekin", "komputer", "kawiatura", 'karta', 'kot', 'pies','myszka', 'procesor']
chances = 5
points = 0
wygenerowane_slowo = hasla[x]
liczba_liter = len(wygenerowane_slowo)
pozostalo = ""
miejsce2 = 0
miejsca = []
i = 1

def convert_list_to_string(org_list, separator = ''):
    return separator.join(org_list)
print('Haslo sklada sie z: '+str(liczba_liter)+' liter')

while(chances != 0 or points == liczba_liter):
    litera = input('Jaka litere wybierasz? ')
    if(len(litera) != 1):
        print("Podaj tylko jedna litere!")
    else:
        if(litera in wygenerowane_slowo):
            miejsce = wygenerowane_slowo.index(litera)
            print('zgadles litere, jest ona na miejcu: '+ str(miejsce))
            points += 1
        else:
            chances -= 1
            if(chances == 0):
                print('Koniec gry. Przegrales!')
            else:
                print("Nie ma takiej litery w hasle!")
                
                if(chances == 1):
                    pozostalo = "Pozostala ci tylko "+str(chances)+" proba"
                elif(chances == 5):
                    pozostalo = "Pozostalo ci tylko "+str(chances)+" prob"
                else:
                    pozostalo = "Pozostaly ci jedynie "+str(chances)+" proby"
                
                print(pozostalo)
        if(liczba_liter == points):
            print('Udalo Ci sie, wygrales! Haslem bylo: '+hasla[x])
            break
        print(hasla[x])

    

