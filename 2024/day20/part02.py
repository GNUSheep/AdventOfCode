from sys import stdin
from collections import defaultdict

grid = []
start = ()
end = ()
path_time = 0
for line in stdin:
    row = []
    for x in range(0, len(line.strip())):
        if line[x] == "S": start = (x, len(grid))
        if line[x] == "E": end = (x, len(grid))
        if line[x] == ".": path_time += 1
        row.append(line[x])
    grid.append(row)

seen = set()
dists = [(path_time, start[0], start[1])]
dists_map = {(start[0], start[1]): path_time}
while True:
    dist, x, y = dists[-1]

    if grid[y][x] == "E":
        break

    seen.add((x,y))

    for nx, ny in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
        if grid[ny][nx] == "#": continue
        if (nx, ny) in seen: continue

        dists.append((dist-1, nx, ny))
        dists_map[(nx, ny)] = dist-1

cheat_map = defaultdict(int)
dists_heap = list(reversed(dists.copy()))

seen = set()
while dists_heap:
    dist, x, y = dists_heap.pop()

    seen.add((x, y))
    for dist_c, x_c, y_c in dists:
        if (x_c, y_c) in seen: continue

        manhattan_dist = abs(x-x_c) + abs(y-y_c)
        if 2 <= manhattan_dist <= 20:
            cheat_map[dist - manhattan_dist - dist_c] += 1  

count = 0
for (k, v) in cheat_map.items():
    if k >= 100:
        count += v
print(count) 
