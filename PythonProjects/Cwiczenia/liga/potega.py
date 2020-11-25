ciag = [3,5,14,13,17,2,6]
potegi = []
wynik = []
y = 1

while y < 10:
    potegi.append(2**y)
    y+=1

for x in ciag:
    if(x in potegi):
        wynik.append(x)

print(wynik)
print(potegi)
print(ciag)
print(2^2)
