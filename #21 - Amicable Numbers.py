def sumDiv(n):
    sum = 1
    p = 2
    while p*p <= n and n > 1:
        if n % p == 0:
            k = p*p
            n //= p
            while n % p == 0:
                k *= p
                n //= p
            sum *= (k-1) // (p-1)
        p += 1 if p == 2 else 2
    if n > 1: sum *= n+1
    return sum

tot = 0
for i in range(1, 10000):
    d = sumDiv(i) - i
    if d > i and sumDiv(d) - d == i:
        tot += i + d

print(tot)