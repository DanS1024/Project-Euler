letters = {1: 3, 2: 3, 3: 5, 4: 4, 5: 4, 6: 3, 7: 5, 8: 5, 9: 4, 10: 3, 11: 6, 12: 6, 13: 8, 14: 8, 15: 7, 16: 7, 17: 9, 18: 8, 19: 8, 20: 6, 30: 6, 40: 5, 50: 5, 60: 5, 70: 7, 80: 6, 90: 6}

def count(n):
    if n in letters:
        return letters[n]
    
    if n < 100:
        return letters[n - n%10] + letters[n%10]
    
    if n < 1000:
        if n % 100 == 0:
            return letters[n//100] + 7
        return letters[n//100] + 7 + 3 + count(n%100)
    
    if n < 10000:
        if n % 1000 == 0:
            return letters[n//1000] + 8
        return letters[n//1000] + 8 + count(n%1000)
    
    return 0

res = 0
for i in range(1, 1001):
    res += count(i)

print(res)