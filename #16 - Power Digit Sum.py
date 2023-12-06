N = 1000

res = [1]
carry = 0
for i in range(N):
    for j in range(len(res)):
        res[j] = 2*res[j] + carry
        carry = res[j] // 10
        res[j] %= 10
    if carry > 0:
        res.append(carry)
        carry = 0

print(sum(res))