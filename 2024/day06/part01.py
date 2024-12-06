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
k = 0

visited = set()
nX = startpos[0] + dirs[k][0]
nY = startpos[1] + dirs[k][1]
while True:
    if grid[nY][nX] == "#":
        nX -= dirs[k][0]
        nY -= dirs[k][1]

        k += 1
        if k == 4:
            k = 0

    visited.add((nX, nY))

    nX += dirs[k][0]
    nY += dirs[k][1]

    if not (0 <= nY < len(grid)) or not (0 <= nX < len(grid[0])):
        break
print(len(visited))
