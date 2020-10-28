import math as m

dane = list(map(float, input("Podaj dane: ").split()))


def Srednia():
    return sum(dane)/len(dane)


srednia = Srednia()

suma = []


def Odchylenie():

    for i in range(0, len(dane)):
        suma.append((dane[i]-srednia)**2)
    odchylenie = m.sqrt((1/(len(dane)-1)*sum(suma)))
    print(odchylenie)
    f = open("wyniki.txt", "a")
    f.write(str(odchylenie)+"\n")
    f.close()


try:
    Odchylenie()
except:
    print("błąd")
    input()
input()
