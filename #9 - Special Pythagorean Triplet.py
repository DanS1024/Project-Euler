N = 1000

for a in range(1, N // 2):
    if N*N % (2*(N-a)) == 0:
        b = N - N*N // (2*(N-a))
        c = N - a - b
        # print(a, b, c)
        print(a*b*c)
        break