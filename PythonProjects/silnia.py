import sys

def silnia(x):
    if x <= 1:
        return 1
    return x * silnia(x-1)
try:
    x = sys.argv[1]
except:
    print("Nie podano argumentu")
    quit()


try:
   print(silnia(int(x)))
except:
   print("Nie podano liczby")
