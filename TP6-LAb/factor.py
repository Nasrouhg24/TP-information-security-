import math
n = 799426357774621
modulus = 799426357774621
for p in range(2, math.isqrt(modulus) + 1):
    if modulus % p == 0:
        q = modulus // p
    
        print("p =", p)
        print("q =", q)
        break