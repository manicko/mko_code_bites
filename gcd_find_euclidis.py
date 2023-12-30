def euclid_GCD(a: int, b: int)-> int:
    a, b = max(a,b), min(a,b)
    while b > 0:
        a, b = b, a % b
    return a


n1 = 23
n2 = 17
print(euclid_GCD(n1, n2))