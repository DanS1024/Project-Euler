N = 100

S = set()
for a in range(2, N+1):
    for b in range(2, N+1):
        S.add(a**b)

print(len(S))