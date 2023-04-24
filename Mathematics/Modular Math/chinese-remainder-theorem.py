#x ≡ 2 mod 5
#x ≡ 3 mod 11
#x ≡ 5 mod 17

from Crypto.Util.number import *

a = [2, 3, 5]
p = [5, 11, 17]

def crt(a, p):
    numerator, denominator = 0, 0;
    for i in range(len(a)):
        n, d = a[i], 1
        for j in range(len(p)):
            if i != j:
                d *= p[j]
        n *= d
        numerator += n
        denominator += d
    N = 1
    for i in range (len(p)):
        N *= p[i]
    return ((numerator % N) * (inverse(denominator, N))) % N 
print(crt(a, p))
