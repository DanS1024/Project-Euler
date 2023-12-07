N = 600851475143

p = 2
while p * p <= N:
    while N % p == 0 and N != p:
        N = N // p
    p += 1 if p == 2 else 2

print(N)