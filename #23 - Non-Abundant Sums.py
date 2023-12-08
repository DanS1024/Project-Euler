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
abundant = []
for i in range(1, 28124):
    a = 0
    b = len(abundant) - 1
    while a <= b:
        if abundant[a] + abundant[b] == i:
            break
        elif abundant[a] + abundant[b] < i:
            a += 1
        else:
            b -= 1
    else:
        tot += i
    
    if sumDiv(i) - i > i:
        abundant.append(i)

print(tot)