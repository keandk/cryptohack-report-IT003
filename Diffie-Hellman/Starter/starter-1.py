p = 991
g = 209

for d in range(1, p):
    if (g * d) % p == 1:
        print(d)
        break
