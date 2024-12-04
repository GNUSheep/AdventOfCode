from sys import stdin

grid = []
for line in stdin:
    line = line.strip()
    grid.append([c for c in line])

n = len(grid[0])
m = len(grid)

def searchWord(r, c):
    word = ""

    if grid[r][c] != "A":
        return 0

    dirs = ((-1, -1, 1, 1),(-1, 1, 1, -1)) 

    x_mas_leg_count = 0
    for r1, c1, r2, c2 in dirs:
        if not (0 <= r+r1 < m) or not (0 <= r+r2 < m):
            continue
        
        if not (0 <= c+c1 < n) or not (0 <= c+c2 < n):
            continue

        if grid[r+r1][c+c1] == "S" and grid[r+r2][c+c2] == "M": 
            x_mas_leg_count += 1      
        elif grid[r+r1][c+c1] == "M" and grid[r+r2][c+c2] == "S":
            x_mas_leg_count += 1

    if x_mas_leg_count == 2:
        return 1
    return 0
        
result = 0
for i in range(0, m):
    for j in range(0, n):
        result += searchWord(i, j)
print(result)
