def euclid_gcd(a: int, b: int) -> int:
    a, b = max(a, b), min(a, b)
    while b > 0:
        a, b = b, a % b
    return a


n1 = 75
n2 = 120
print(75 * 120 / euclid_GCD(n1, n2))
