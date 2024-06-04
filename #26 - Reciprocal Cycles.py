N = 1000

def sieve(n):
    primes = [True] * n
    primes[0] = primes[1] = False
    for i in range(2, n):
        if primes[i]:
            for j in range(i*i, n, i):
                primes[j] = False
    return [i for i, p in enumerate(primes) if p]

primes = sieve(N)

def order(p, b=10):
    i = 1
    m = b % p
    while m > 1:
        m *= b
        m %= p
        i += 1
    return i

d, l = 0, 0
for p in primes:
    l, d = max((l, d), (order(p), p), key=lambda t: t[0])

print(d)