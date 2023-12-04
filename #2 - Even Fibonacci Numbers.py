a, b = 0, 2
tot = 0
while b < 4000000:
    tot += b
    a, b = b, 4*b + a
print(tot)