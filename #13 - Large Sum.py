with open("Project Euler/input.txt") as f:
    data = f.read().split("\n")

i = 0
tot = ''
carry = 0

while i < len(data[0]):
    s = 0
    for num in data:
        s += int(num[-1-i])
    tot += str((s+carry) % 10)
    carry = (s+carry) // 10
    i += 1

if carry > 0: tot += str(carry)[::-1]
tot = tot[::-1]

print(tot[:10])