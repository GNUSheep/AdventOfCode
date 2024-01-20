from sys import stdin

trails = []
for line in stdin:
    trails.append(list(line.rstrip()))

# y x
queue = [(0,1,0,0)]
seen = []

dists = set()

while queue:
    y, x, dist, index = queue.pop()
    seen = seen[:index]

    if y == len(trails) - 1 and x == len(trails[0]) - 2:
        dists.add(dist)
        continue

    if (y, x) in seen:
        continue
    seen.append((y, x))

    if trails[y][x] in "><v^":
        if trails[y][x] == ">":
            queue.append((y, x+1, dist+1, index+1))
        elif trails[y][x] == "<":
            queue.append((y, x-1, dist+1, index+1))
        elif trails[y][x] == "^":
            queue.append((y-1, x, dist+1, index+1))
        elif trails[y][x] == "v":
            queue.append((y+1, x, dist+1, index+1))
    else:
        for y_dir, x_dir in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            if 0 <= y+y_dir < len(trails) and 0 <= x+x_dir < len(trails[0]) and trails[y+y_dir][x+x_dir] != "#" and (y_dir+y, x+x_dir) not in seen:
                queue.append((y+y_dir, x+x_dir, dist+1, index+1))
print(max(dists))