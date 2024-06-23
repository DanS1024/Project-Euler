aMax, bMax = 1000, 1000

def sieve(n):
    primes = [True] * n
    primes[0] = primes[1] = False
    for i in range(2, n):
        if primes[i]:
            for j in range(i*i, n, i):
                primes[j] = False
    return primes

def f(n, a, b):
    return (n + a)*n + b

def consec(a, b):
    n = 0
    y = f(n, a, b)
    while y >= 2 and primes[y]:
        n += 1
        y = f(n, a, b)
    return n

primes = sieve(f(bMax, aMax, bMax))

n_, a_, b_ = 0, 0, 0
for a in range(-aMax, aMax+1):
    for b in range(2, bMax+1):
        n = consec(a, b)
        if n > n_:
            n_, a_, b_ = n, a, b

print(a_ * b_)