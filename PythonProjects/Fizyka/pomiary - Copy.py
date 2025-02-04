import math as m
import sys
# dane = list(map(float, input("Podaj dane: ").split()))
# masa = int(input("Podaj mase ciala: "))
# a = float(input("Podaj przyspieszenie: "))
# minm, maxm = float, input("Podaj najmniejsza i największą mase: ").split()
# mina, maxa = float, input(
#     "Podaj najmniesze i nawiększe przyspieszenie: ").split()
try:
    f = open("pomiary.txt", "r")
    dane = f.readline().replace("\n", "")
    dane = dane.split(sep=',')
    for i in range(0, len(dane)):
        dane[i] = float(dane[i])
    a = f.readline().replace("\n", "")
    a = a.split(sep=",")
    for i in range(0, len(a)):
        a[i] = float(a[i])
    print(dane, a)
except:
    print("Blad")
    exit()
# dane = [4.2907, 4.2407, 4.4031, 4.2300, 4.2885, 4.4385, 4.1808, 4.2838, 4.3130, 4.2107,
#         4.4749, 4.2871, 4.3892, 4.3058, 4.4444, 4.3057, 4.4208, 4.3240]  # masa podana w kg
# a = [19.8, 20.01, 20.81, 18.9]  # przyspieszenie podane w m/s2


def Srednia(cos):
    return sum(cos)/len(cos)


def Silah():
    fmin = (Srednia(dane)-wachanie_masy) * \
        ((Srednia(a)-wachanie_przyspieszenia)+9.81)
    fmax = (Srednia(dane)+wachanie_masy) * \
        ((Srednia(a)+wachanie_przyspieszenia)+9.81)
    print(fmin, fmax)
    return (fmax - fmin)/2


def BladPomiaru(co):
    return (max(co)-min(co))/2


def Odchylenie(pomiar):
    for i in range(0, len(pomiar)):
        suma.append((pomiar[i]-Srednia(pomiar))**2)
    return m.sqrt((1/(len(pomiar)-1)*sum(suma)))


suma = []
srednia = Srednia(dane)
wachanie_masy = 0.001
wachanie_przyspieszenia = BladPomiaru(a)
f = open("wyniki.txt", "w")
print("Średnia siła hamowania wynosi: " +
      str(Srednia(dane)*(Srednia(a)+9.81))+"N\n")
f.write("Średnia siła hamowania wynosi: " +
        str(Srednia(dane)*(Srednia(a)+9.81))+"N\n")
f.write("Wartość odchylenia wynosi: "+str(Odchylenie(dane))+"kg\n")
f.write("Wartość odchylenia standardowego przyspieszenia wynosi : " +
        str(Odchylenie(a))+"m/s2\n")
f.write("Niepewność siły hamowania wynosi: "+str(Silah())+"N\n")
f.write("Niepewność pomiarowa przyspieszenia wynosi: " +
        str(wachanie_przyspieszenia)+"m/s2\n")
f.close()

