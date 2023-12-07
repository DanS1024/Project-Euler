primes = [2]
count = 1
n = 3
while count < 10001:
    for p in primes:
        if n % p == 0:
            break
        elif p*p > n:
            primes.append(n)
            count += 1
            break
    n += 2
print(primes[-1])