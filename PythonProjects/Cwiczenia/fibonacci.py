#program do tworzenia liczb z ciagu fibbonaciego 


def wygeneruj_fibonacci(x):
    liczba1 = 0
    liczba2 = 1
    while x >= 0: 
        print(liczba2)
        liczba1 = liczba1 + liczba2
        print(liczba1)
        liczba2 = liczba1 + liczba2
        x-=1

ile_razy = input("Ile liczb Fibonacciego mam pokazac? ")
ile_razy = int(ile_razy)
wygeneruj_fibonacci(ile_razy)