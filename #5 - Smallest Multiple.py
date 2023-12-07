N = 20

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

primes = sieve(N)

maxPow = [0] * len(primes)
for i, p in enumerate(primes):
    n = p
    while n <= N:
        maxPow[i] += 1
        n *= p

ans = 1
for p, e in zip(primes, maxPow):
    ans *= p**e

print(ans)