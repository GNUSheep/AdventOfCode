from sys import stdin

keys = []
locks = []

h = 7
w = 5
        
lines = [line.strip() for line in stdin.readlines()]

for i in range(0, len(lines), 8):
    is_key = True if lines[i][0] != "#"  else False

    map = [0] * w
    for r in range(0, h):
        for c in range(0, w):
            if lines[i+r][c] == "#":
                map[c] += 1
    if is_key:
        keys.append(map)
    else:
        locks.append(map)

unique_pairs = 0
for lock in locks:
    for key in keys:
        for i in range(0, w):
            if lock[i] + key[i] > 7:
                break
        else:
            unique_pairs += 1
            continue
        continue
print(unique_pairs)
