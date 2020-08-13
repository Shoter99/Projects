import random as rand
import time

x = rand.randint(0,8)
hasla = ['REKIN', 'KOMPUTER', 'KRZESŁO', 'SŁOWNIK', 'KACZKA', 'APARAT', 'TELEFON', 'SZKOŁA', 'PIES']
chances = 5
points = 0
wygenerowane_slowo = hasla[x]
liczba_liter = len(wygenerowane_slowo)
pozostalo = ""
miejsce2 = 0
miejsca = []
i = 1
guessed = []

def convert_list_to_string(org_list, separator = ''):
    return separator.join(org_list)
print('Haslo sklada sie z: '+str(liczba_liter)+' liter')

while(chances != 0 or points == liczba_liter):
    litera = input('Jaka litere wybierasz? ').upper()
    guessed.append(litera)
    if litera not in wygenerowane_slowo:
        chances -= 1
    if(len(litera) != 1):
        print("Podaj tylko jedna litere!")
    else:
        display_word = ""
        for letter in wygenerowane_slowo:
            if letter in guessed:
                display_word += letter + ' '
            else:
                display_word += '_ '
        print(display_word)
        if(chances == 0):
                print('Koniec gry. Przegrales!')
       
                
    if(chances == 1):
                   pozostalo = "Pozostala ci tylko "+str(chances)+" proba"
    elif(chances == 5):
             pozostalo = "Pozostalo ci tylko "+str(chances)+" prob"
    else:
                  pozostalo = "Pozostaly ci jedynie "+str(chances)+" proby"
    print(pozostalo)
    haslo = display_word.split(" ")
    haslo = convert_list_to_string(haslo, "")
    if(wygenerowane_slowo == haslo):
        print('Udalo Ci sie, wygrales! Haslem bylo: '+hasla[x])
        break
     

    

