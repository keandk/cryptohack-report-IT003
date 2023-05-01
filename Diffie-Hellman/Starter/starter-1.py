def extended_euclidean_algorithm(a, b):
    r0, r1 = a, b
    t0, t1 = 0, 1

    while r1 != 0:
        q = r0 // r1
        r0, r1 = r1, r0 % r1
        t0, t1 = t1, t0 - q * t1

    return r0, t0

def modular_inverse(g, p):
    gcd, t = extended_euclidean_algorithm(g, p)

    if gcd != 1:
        raise ValueError("g and p are not coprime")

    return t % p

p = 991
g = 209

for d in range(1, p):
    if (g * d) % p == 1:
        print(d)
        break
