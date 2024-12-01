from sys import stdin

trails = []
for line in stdin:
    trails.append(list(line.rstrip()))

# y x
points = [(0,1), (len(trails)-1, len(trails[0])-2)]

for y in range(len(trails)):
    for x in range(len(trails[0])):
        if trails[y][x] == "#":
            continue

        neigbours = 0
        for y_dir, x_dir in ((0,1), (0,-1), (1,0), (-1,0)):
            if 0 <= y_dir+y < len(trails) and 0 <= x_dir+x < len(trails[0]) and trails[y_dir+y][x_dir+x] != "#":
                neigbours += 1

        if neigbours >= 3:
            points.append((y, x))

graph = {i: {} for i in points}
for sy, sx in points:
    queue = [(sy, sx, 0)]
    seen = {(sy, sx)}

    while queue:
        y, x, dist = queue.pop()

        if dist != 0 and (y, x) in points:
            graph[(sy, sx)][(y, x)] = dist
            continue

        for y_dir, x_dir in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            if 0 <= y+y_dir < len(trails) and 0 <= x+x_dir < len(trails[0]) and trails[y+y_dir][x+x_dir] != "#" and (y_dir+y, x+x_dir) not in seen:
                queue.append((y+y_dir, x+x_dir, dist+1))
                seen.add((y+y_dir, x+x_dir))

seen = set()
def dfs(point):
    if point == (len(trails)-1, len(trails[0])-2):
        return 0

    dist = -float("inf")

    seen.add(point)
    for point_next in graph[point]:
        if point_next not in seen:
            dist = max(dist, dfs(point_next)+graph[point][point_next])
    seen.remove(point)

    return dist

print(dfs((0,1)))