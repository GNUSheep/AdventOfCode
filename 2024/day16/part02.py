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
dist_s = {}
lowest_score = -1

while moves:
    score, x, y, dir_x, dir_y = heapq.heappop(moves)
    
    if (x, y, dir_x, dir_y) not in dist_s:
        dist_s[(x, y, dir_x, dir_y)] = score
    
    if (x, y) == end and lowest_score == -1:
        lowest_score = score
    
    if (x, y, dir_x, dir_y) in seen:
        continue
    seen.add((x, y, dir_x, dir_y))
    
    nx, ny = x + dir_x, y + dir_y
    if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] != '#':
        heapq.heappush(moves, (score + 1, nx, ny, dir_x, dir_y))

    left_dir = (-dir_y, dir_x)
    right_dir = (dir_y, -dir_x)
    heapq.heappush(moves, (score + 1000, x, y, left_dir[0], left_dir[1]))
    heapq.heappush(moves, (score + 1000, x, y, right_dir[0], right_dir[1]))

moves = [
    (0, end[0], end[1], 1, 0),
    (0, end[0], end[1], -1, 0),
    (0, end[0], end[1], 0, 1),
    (0, end[0], end[1], 0, -1),
]
seen = set()
dist_e = {}

while moves:
    score, x, y, dir_x, dir_y = heapq.heappop(moves)
    if (x, y, dir_x, dir_y) not in dist_e:
        dist_e[(x, y, dir_x, dir_y)] = score
 
    if (x, y, dir_x, dir_y) in seen:
        continue
    seen.add((x, y, dir_x, dir_y))
    
    nx, ny = x - dir_x, y - dir_y
    if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] != '#':
        heapq.heappush(moves, (score + 1, nx, ny, dir_x, dir_y))
    
    left_dir = (-dir_y, dir_x)
    right_dir = (dir_y, -dir_x)
    heapq.heappush(moves, (score + 1000, x, y, left_dir[0], left_dir[1]))
    heapq.heappush(moves, (score + 1000, x, y, right_dir[0], right_dir[1]))

path = set()
for y in range(0, len(grid)):
    for x in range(0, len(grid[0])):
        for dir in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            if (x,y,dir[0], dir[1]) in dist_s and (x,y,dir[0], dir[1]) in dist_e and dist_s[(x, y, dir[0], dir[1])] + dist_e[(x, y, dir[0], dir[1])] == lowest_score:
                path.add((x, y))
print(len(path)) 
