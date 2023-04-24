p = 29
ints = [14, 6, 11]

def getQuaratic(x):
    for a in range (p):
        if pow(a, 2, p) == x:
            return a
    return -1

for x in ints:
    a = getQuaratic(x)
    if a != -1:
        print(a)
