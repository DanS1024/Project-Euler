def isProduct(n):
    i = 999
    while i * i >= n:
        if n % i == 0 and n // i < 1000:
            return True
        i -= 1
    return False

for p in range(999, 99, -1):
    n = int(str(p) + str(p)[::-1])
    if isProduct(n):
        print(n)
        break