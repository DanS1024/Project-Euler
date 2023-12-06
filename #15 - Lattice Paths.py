N = 20

res = 1
for i in range(1, N+1):
    res *= N+i
    res //= i

print(res)