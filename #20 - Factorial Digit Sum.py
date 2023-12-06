N = 100

res = [1]
carry = 0
for i in range(N, 0, -1):
    for j in range(len(res)):
        res[j] = i*res[j] + carry
        carry = res[j] // 10
        res[j] %= 10
    if carry > 0:
        res += list(map(int, str(carry)))[::-1]
        carry = 0

print(sum(res))