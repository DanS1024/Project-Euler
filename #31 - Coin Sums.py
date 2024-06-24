coins = [1, 2, 5, 10, 20, 50, 100, 200]
tot = 200

res = 0
def comb(r, i):
    global coins, res
    if i == 0:
        if r % coins[i] == 0:
            res += 1
        return
    for k in range(r//coins[i]+1):
        comb(r - k*coins[i], i-1)

comb(tot, len(coins)-1)
print(res)
