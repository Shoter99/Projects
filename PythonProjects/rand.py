from random import randint

x = []
for _ in range(20):
    x.append(str(randint(0,9)))
print("".join(x))
