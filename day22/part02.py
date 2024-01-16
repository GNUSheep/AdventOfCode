from collections import deque
from sys import stdin

def collision(a, b):
    return max(a[0], b[0]) <= min(a[3], b[3]) and max(a[1], b[1]) <= min(a[4], b[4])

bricks = []
for line in stdin:
    bottom, upper = line.rstrip().split("~")
    bricks.append(list(map(int, bottom.split(","))) + list(map(int, upper.split(","))))

bricks.sort(key=lambda bricks: bricks[2])


for index in range(len(bricks)):
    how_far_can_fall = 1
    for next_brick in bricks[:index]:
        if collision(bricks[index], next_brick):
            how_far_can_fall = max(how_far_can_fall, next_brick[5]+1)
    bricks[index][5] -= bricks[index][2] - how_far_can_fall
    bricks[index][2] = how_far_can_fall

bricks.sort(key=lambda brick: brick[2])

supports = [{x: set() for x in range(len(bricks))}, {x: set() for x in range(len(bricks))}]

for i in range(len(bricks)):
    for j in range(len(bricks[:i])):
        if collision(bricks[j], bricks[i]) and bricks[i][2] == bricks[j][5] + 1:
            supports[0][j].add(i)
            supports[1][i].add(j)

total = 0

for i in range(len(bricks)):
    queue = deque(brick for brick in supports[0][i] if len(supports[1][brick]) == 1)
    falling = set(queue)
    falling.add(i)

    while queue:
        brick = queue.popleft()
        for x in supports[0][brick] - falling:
            if supports[1][x] <= falling:
                queue.append(x)
                falling.add(x)
    
    total += len(falling) - 1

print(total)