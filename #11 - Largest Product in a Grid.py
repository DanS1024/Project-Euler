with open("Project Euler/input.txt") as f:
    data = f.read().split("\n")

grid = []
for line in data:
    grid.append(list(map(int, line.split())))

N = 4
ans = 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if i+N <= len(grid):
            prod = 1
            for k in range(N):
                prod *= grid[i+k][j]
            ans = max(ans, prod)
        
        if j+N <= len(grid[i]):
            prod = 1
            for k in range(N):
                prod *= grid[i][j+k]
            ans = max(ans, prod)
        
        if i+N <= len(grid) and j+N <= len(grid[i]):
            prod = 1
            for k in range(N):
                prod *= grid[i+k][j+k]
            ans = max(ans, prod)
            
            prod = 1
            for k in range(N):
                prod *= grid[i+N-1-k][j+k]
            ans = max(ans, prod)

print(ans)