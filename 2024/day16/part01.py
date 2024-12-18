from sys import stdin
import heapq

grid = []
end = (0, 0)
start = (0, 0)
for line in stdin:
    r = []
    for x in range(0, len(line.strip())):
        if line[x] == "E": end = (x, len(grid))
        elif line[x] == "S": start = (x, len(grid))
        
        r.append(line[x])
    grid.append(r)

moves = [(0, start[0], start[1], 1, 0)]
seen = set()
while moves:
    score, x, y, dir_x, dir_y = heapq.heappop(moves)
    
    if (x, y) == end:
        print(score)
        break

    if (x, y, dir_x, dir_y) in seen:
        continue
    seen.add((x, y, dir_x, dir_y))

    nx, ny = x + dir_x, y + dir_y
    if 0 <= nx < len(grid[0]) and 0 <= ny < len(grid) and grid[ny][nx] != '#':
        heapq.heappush(moves, (score + 1, nx, ny, dir_x, dir_y))

    left_dir = (-dir_y, dir_x)
    right_dir = (dir_y, -dir_x)
    heapq.heappush(moves, (score + 1000, x, y, left_dir[0], left_dir[1]))
    heapq.heappush(moves, (score + 1000, x, y, right_dir[0], right_dir[1]))