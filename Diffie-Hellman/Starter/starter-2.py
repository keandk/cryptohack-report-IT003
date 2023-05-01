p = 28151
for g in range(1, p):
    print('g:', g)
    h = set()
    for n in range(p):
        h.add(pow(g, n, p))
    # print(h)
    # the set must contain all *nonzero* elements of Fp
    if set(range(1, p)).issubset(h):
        print(g)
        break