liczby = [2,4,5,6,10,14,3,27,9,17]
dzielniki = []
wyniki = []
y = 20
x = 1
while x < y:
    dzielniki.append(x)
    x +=1

for z in dzielniki:
    for l in liczby:
        if((l/z)%2 == 0 or (l/z)%2 == 1):
            if (l not in wyniki):
                wyniki.append(l)

print(3/1%2)
print(wyniki)