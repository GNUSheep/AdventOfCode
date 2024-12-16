from sys import stdin

grid = {"#": [], "O": {}, "L": {}, "R": {}}

y = 0
pos = ()
for line in stdin:
    if line == "\n": break
    line = line.strip()
    x = 0
    for i in range(0, len(line)):
        if line[i] == "@":
            pos = (x, y)
            x += 1
        elif line[i] == "#":
            grid["#"].append((x, y))        
            grid["#"].append((x+1, y))
            x += 1
        elif line[i] == "O":
            grid["O"][(x, y)] = 1
            grid["O"][(x+1, y)] = 1
            grid["L"][(x, y)] = 1
            grid["R"][(x+1, y)] = 1
            
            x += 1
        else:
            x += 1
        x += 1
    
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

    if n_pos in grid["O"] and move in "<>":
        steps = [(n_pos[0], n_pos[1])]
        while steps[-1] in grid["O"]:
            steps.append((steps[-1][0] + dir[0], steps[-1][1] + dir[1]))
        
        if steps[-1] in grid["#"]: continue
        
        for step in reversed(steps[:-1]):
            grid["O"].pop(step)
            
            grid["O"][(step[0] + dir[0], step[1] + dir[1])] = 1
            if step in grid["L"]:
                grid["L"].pop(step)    
                grid["L"][(step[0] + dir[0], step[1] + dir[1])] = 1
            else:                
                grid["R"].pop(step)    
                grid["R"][(step[0] + dir[0], step[1] + dir[1])] = 1

    if n_pos in grid["O"] and move in "^v":
        steps = set()
        steps.add((n_pos[0], n_pos[1]))
        if n_pos in grid["L"]: steps.add((n_pos[0] + 1, n_pos[1]))
        if n_pos in grid["R"]: steps.add((n_pos[0] - 1, n_pos[1]))
            
        mv = list(steps.copy())
        while len(mv) != 0:
            m = mv.pop()

            nw_pos = (m[0]+dir[0], m[1]+dir[1])
            if nw_pos in grid["O"]:
                mv.append(nw_pos)
                steps.add(nw_pos)
                
                if nw_pos in grid["L"]: 
                    steps.add((nw_pos[0] + 1, nw_pos[1]))
                    mv.append((nw_pos[0] + 1, nw_pos[1]))
                if nw_pos in grid["R"]: 
                    steps.add((nw_pos[0] - 1, nw_pos[1]))
                    mv.append((nw_pos[0] - 1, nw_pos[1]))

        if move == "v": steps = sorted(steps, key=lambda x: x[1], reverse=False)
        else: steps = sorted(steps, key=lambda x: x[1], reverse=True)

        for step in reversed(list(steps)):
            if (step[0] + dir[0], step[1] + dir[1]) in grid["#"]: break
            
            if not ((step[0] + dir[0], step[1] + dir[1]) in steps) and (step[0] + dir[0], step[1] + dir[1]) in grid["O"]: break 
        else: 
            for step in reversed(list(steps)):
              grid["O"].pop(step)

              grid["O"][(step[0] + dir[0], step[1] + dir[1])] = 1
              if step in grid["L"]:
                  grid["L"].pop(step)    
                  grid["L"][(step[0] + dir[0], step[1] + dir[1])] = 1
              else:                
                  grid["R"].pop(step)    
                  grid["R"][(step[0] + dir[0], step[1] + dir[1])] = 1
    if not n_pos in grid["O"] and not n_pos in grid["#"]:      
        pos = n_pos
        
coordinates = 0
for box in grid["L"]:
    coordinates += box[1] * 100 + box[0]

print(coordinates)
