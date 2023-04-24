from Crypto.Util.number import inverse
r = [588, 665, 216, 113, 642, 4, 836, 114, 851, 492, 819, 237]
lowerbound = max(r) + 1
for p in range (lowerbound, 999):
    try:
        x = [(r[i] * inverse(r[i - 1], p)) % p for i in range (1, 11)]
        if (len(set(x)) == 1):
            print(p, x)
            break
    except:
        pass
