def sieve(n):
    primes = [True] * (n+1)
    primes[0] = primes[1] = False
    p = 2
    while p*p <= n:
        if primes[p]:
            for j in range(p*p, n+1, p):
                primes[j] = False
        p += 1 if p == 2 else 2
    return [i for i, v in enumerate(primes) if v]

primes = sieve(500)

def numDiv(n):
    ans = 1
    for p in primes:
        if p*p > n: break
        e = 0
        while n % p == 0:
            e += 1
            n //= p
        ans *= e+1
    if n > 1: ans *= 2
    return ans

n = 1
while numDiv(n*(n+1)//2) <= 500:
    n += 1

print(n*(n+1)//2)