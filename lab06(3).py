def isOddNumberPrime(n):
    for x in range(3, n, 2):
        if x*x > n:
            return True
        if n % x == 0:
            return False

p = [x for x in range(3, 100, 2) if isOddNumberPrime(x)]
p4s = {x**4 for x in p}

for n in range(45000000, 50000000 + 1):
    x = n
    while (x & 1) == 0:
        x >>= 1
    if x in p4s:
        print(n)