def sieve(n):
    primes = [True] * (n+1)
    primes[0] = primes[1] = False
    i = 2
    while i*i <= n:
        if primes[i]:
            for j in range(i*i, n+1, i):
                primes[j] = False
        i += 1
    return [i for i, p in enumerate(primes) if p]

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
while numDiv(n*(n+1)//2) <= 500: n += 1

print(n*(n+1)//2)