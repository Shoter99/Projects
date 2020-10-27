

print("Pomyśl o jakieś liczbie od 1 do 100")


def Check():
    num = [i+1 for i in range(0, 100)]
    x = input("Czy twoja liczba jest większa, czy mniejsza niż " +
              str(int(len(num)/2)) + ": ")
    l1 = [i+1 for i in range(min(num), int(max(num)/2))]
    l2 = [i+1 for i in range(int(max(num)/2, max(num)))]
    if x.lower() == 'mniejsza' or x.lower() == 'mniejszy':
        num = l1
        Check()
    elif x.lower() == 'wieksza' or x.lower() == 'większa':
        num = l2
        Check()
    elif x.lower() == 'równa' or x.lower() == 'rowna':
        print("Twoja liczba to" + str(x)+"!")


Check()
