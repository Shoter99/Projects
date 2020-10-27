def getNthFib(n):

    seq = []
    f0 = 0
    f1 = 1
    for i in range(0, n):
        seq.append(f0)
        seq.append(f1)
        f0 = f1 + f0
        f1 = f0 + f1
    print(seq[n-1])


getNthFib(6)
