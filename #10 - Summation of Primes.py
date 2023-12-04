def sieve(n):
    primes = [True] * n
    primes[0] = primes[1] = False
    for i in range(2, n):
        if primes[i]:
            for j in range(i*i, n, i):
                primes[j] = False
    return [i for i, p in enumerate(primes) if p]

primes = sieve(2000000)
tot = sum(primes)
print(tot)