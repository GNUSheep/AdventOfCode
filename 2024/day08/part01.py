from sys import stdin

frequency = {}
max_y = 0
max_x = 0
grid = []
for line in stdin:
    line = line.strip()

    col = []
    max_x = len(line)
    for i in range(0, len(line)):
        if line[i] != ".":
            if not (line[i] in frequency):
                frequency[line[i]] = [(i, max_y)]
            else:
                frequency[line[i]].append((i, max_y))
        col.append(line[i])
    grid.append(col)

    max_y += 1

antiodes = set()
for (key, value) in frequency.items():
    for i in range(0, len(value)):
        for j in range(i, len(value)):
            if i == j:
                continue
            
            dist_x, dist_y = value[i][0] - value[j][0], value[i][1] - value[j][1]

            if 0 <= value[i][0] + dist_x < max_x and 0 <= value[i][1] + dist_y < max_y:                 
                antiodes.add((value[i][0] + dist_x, value[i][1] + dist_y))
                      
            if 0 <= value[j][0] - dist_x < max_x and 0 <= value[j][1] - dist_y < max_y: 
                antiodes.add((value[j][0] - dist_x, value[j][1] - dist_y))
print(len(antiodes))
