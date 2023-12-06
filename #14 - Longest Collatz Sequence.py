N = 1000000

moves = [0] * N
moves[1] = 1

def collatz(n):
    if n < N and moves[n] != 0:
        return moves[n]
    
    if n % 2 == 0:
        m = 1 + collatz(n//2)
        if n < N:
            moves[n] = m
        return m
    
    m = 1 + collatz(3*n+1)
    if n < N:
        moves[n] = m
    return m

maxn, maxm = 1, 0
for n in range(N, 0, -1):
    m = collatz(n)
    if m > maxm:
        maxn, maxm = n, m

print(maxn, maxm)