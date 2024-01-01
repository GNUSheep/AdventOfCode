from sys import stdin
from heapq import heappop, heappush

grid = []
for line in stdin:
    grid.append(tuple(line.rstrip()))

# up, right, down, left
dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]

paths = [(0, 0, 0, (0, 0), 0)]
seen = set()

while paths:
    heat_loss, x, y, direction, num_of_steps = heappop(paths)
    if x == len(grid) - 1 and y == len(grid[0]) - 1:
        print(heat_loss)
        break

    if (x, y, direction, num_of_steps) in seen:
        continue
    seen.add((x, y, direction, num_of_steps))

    if num_of_steps < 3 and direction != (0, 0):
        if 0 <= x+direction[0] < len(grid) and 0 <= y+direction[1] < len(grid[0]):
            heappush(paths, (heat_loss+int(grid[x+direction[0]][y+direction[1]]), x+direction[0], y+direction[1], direction, num_of_steps + 1))
    
    for dir_ in dirs:
        if dir_ != direction and dir_ != (-direction[0], -direction[1]):
            if 0 <= x+dir_[0] < len(grid) and 0 <= y+dir_[1] < len(grid[0]):
                heappush(paths, (heat_loss+int(grid[x+dir_[0]][y+dir_[1]]), x+dir_[0], y+dir_[1], dir_, 1))