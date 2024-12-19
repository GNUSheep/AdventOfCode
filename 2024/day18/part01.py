from sys import stdin
import heapq

width = 71
height = 71

grid = [["."] * width for _ in range(0, height)]

for line in stdin:
    x,y = line.strip().split(",")

    grid[int(y)][int(x)] = "#"

moves = [(0, 0, 0)]
seen = set()
while moves:
    steps, x, y = heapq.heappop(moves)

    if (x, y) == (70,70):
        print(steps)
        break

    if (x, y) in seen:
        continue
    seen.add((x, y))

    for nx, ny in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
        if not 0 <= nx < width or not 0 <= ny < height:
            continue
        if grid[ny][nx] == "#": continue

        heapq.heappush(moves, (steps+1, nx, ny))
