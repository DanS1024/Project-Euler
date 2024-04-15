N = 1000000
digits = 10

N -= 1

total = 1
for i in range(1, digits+1):
    total *= i

res = ''
order = list(range(digits))
for i in range(digits, 0, -1):
    total //= i
    res += str(order[N // total])
    del order[N // total]
    N %= total

print(res)