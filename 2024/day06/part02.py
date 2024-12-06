from sys import stdin

grid = []
startpos = ()
for line in stdin:
    col = []
    for x in line.strip():
        if x == "^":
            startpos = (line.index(x), len(grid))
        col.append(x)
    grid.append(col)

dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]

def check_loop(new_grid):
    visited = set()
    k = 0
    nX = startpos[0] + dirs[k][0]
    nY = startpos[1] + dirs[k][1]
    while True:
        if new_grid[nY][nX] == "#":
            nX -= dirs[k][0]
            nY -= dirs[k][1]

            k += 1
            if k == 4:
                k = 0

        if (nX, nY, k) in visited:
            return True
    
        visited.add((nX, nY, k))

        nX += dirs[k][0]
        nY += dirs[k][1]

        if not (0 <= nY < len(grid)) or not (0 <= nX < len(grid[0])):
            return False

loop_counted = 0
for y in range(len(grid)):
    for x in range(len(grid[0])):
        if grid[y][x] == ".":
            if startpos == (x, y):
                continue

            grid[y][x] = "#" 
            if check_loop(grid):
                loop_counted += 1
            grid[y][x] = "."
print(loop_counted)     
