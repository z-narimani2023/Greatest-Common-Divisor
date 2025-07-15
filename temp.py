
def gcd(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a


print("ب.م.م دو عدد =", gcd(12,18))
