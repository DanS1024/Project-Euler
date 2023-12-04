N = 20

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