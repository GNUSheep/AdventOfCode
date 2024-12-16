from sys import stdin

grid = {"#": [], "O": {}}
y = 0
x_m = 0
pos = ()
for line in stdin:
    if line == "\n": break
    x_m = len(line.strip())
    line = line.strip()
    for x in range(0, len(line)):
        if line[x] == "@":
            pos = (x, y)
        elif line[x] == "#":
            grid["#"].append((x, y))
        elif line[x] == "O":
            grid["O"][(x, y)] = 1  
    y += 1

moves = ""
for line in stdin:
    moves += line.strip()
    
for move in moves:
    dir = ()
    if move == "^": dir = (0, -1)
    elif move == "v": dir = (0, 1)
    elif move == "<": dir = (-1, 0)
    if move == ">": dir = (1, 0)

    n_pos = (pos[0] + dir[0], pos[1] + dir[1])

    if n_pos in grid["#"]: continue

    if n_pos in grid["O"]:
        steps = [(n_pos[0], n_pos[1])]
        while steps[-1] in grid["O"]:
            steps.append((steps[-1][0] + dir[0], steps[-1][1] + dir[1]))
        
        if steps[-1] in grid["#"]: continue
        
        for step in reversed(steps[:-1]):
            grid["O"].pop(step)
            grid["O"][(step[0] + dir[0], step[1] + dir[1])] = 1
    pos = n_pos

coordinates = 0
for box in grid["O"]:
    coordinates += box[1] * 100 + box[0]
print(coordinates)
