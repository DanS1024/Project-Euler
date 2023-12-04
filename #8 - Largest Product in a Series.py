N = 13

with open("Project Euler/input.txt") as f:
    data = f.read().split("\n")
num = "".join(data)

def next(n):
    global i
    if i+N > len(num):
        i = len(num)
        return 0
    n = 1
    for j in range(N):
        n *= int(num[i+j])
        if n == 0:
            i += j+1
            n = next(n)
            break
    return n

i = 0
prod = next(0)
ans = prod
while i+N < len(num):
    prod //= int(num[i])
    prod *= int(num[i+N])
    i += 1
    if prod == 0:
        prod = next(prod)
    ans = max(ans, prod)

print(ans)