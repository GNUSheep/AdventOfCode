from sys import stdin
import re

robots = []
for line in stdin:
    px,py,vx,vy = [int(x) for x in re.findall(r"-?\d+", line.strip())]

    robots.append([px,py,vx,vy])

width = 11
height = 7


grid = [[0] * width for _ in range(0, height)]
for robot in robots:
    px,py,vx,vy = robot[0], robot[1], robot[2], robot[3]
    for _ in range(0, 10):
        n_px = px + vx
        n_py = py + vy

        if not (0 <= n_px < 11):
            n_px = width - n_px

        grid[py][px] = 0
        px = n_px
        grid[py][px] = 1
        print(80*"=")
        for c in grid:
            print(c)
# for c in grid:
    # print(c)
