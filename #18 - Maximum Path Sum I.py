with open("Project Euler/input.txt") as f:
    data = f.read().split("\n")

triangle = [list(map(int, line.split(" "))) for line in data]

total = [0] * len(triangle)
for i in range(len(triangle)):
    for j in range(i, 0, -1):
        total[j] = max(total[j], total[j-1]) + triangle[i][j]
    total[0] += triangle[i][0]

print(max(total))