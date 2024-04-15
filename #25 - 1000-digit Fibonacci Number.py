L = 1000

i, a, b = 1, 1, 1
while len(str(a)) < L:
    a, b = b, a + b
    i += 1

print(i)