from sys import stdin
from collections import defaultdict

grid = []
for line in stdin:
    grid.append([plant for plant in line.strip()])

seen = set()
plant_map = []
for y in range(0, len(grid)):
    for x in range(0, len(grid[0])): 
        moves = [(y, x)]

        if (y,x) in seen:
            continue
        plant = []        
        while len(moves) != 0:
            move = moves.pop()
            
            if (move[0], move[1]) in seen:
                continue
            seen.add((move[0], move[1]))

            plant.append([move[0], move[1]])
            
            # up, down, left, right y x
            for dir in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                n_y = move[0]+dir[0]
                n_x = move[1]+dir[1]

                if 0 <= n_x < len(grid[0]) and 0 <= n_y < len(grid):
                    if grid[n_y][n_x] == grid[move[0]][move[1]] and not ((n_y, n_x) in seen):
                        moves.append((n_y, n_x))
        
        if len(plant) != 0:
            plant_map.append(plant)
price = 0    
for plant in plant_map:
    corners = set()
    for (y, x) in plant:
        for dir in ((0.5, 0.5), (-0.5, 0.5), (0.5, -0.5), (-0.5, -0.5)):
            corners.add((y+dir[0], x+dir[1]))

    corners_count = 0
    for (y, x) in corners:
        variants = []
        for n_y, n_x in [(y - 0.5, x - 0.5), (y + 0.5, x - 0.5), (y + 0.5, x + 0.5), (y - 0.5, x + 0.5)]:
            variants.append([n_y, n_x] in plant)

        number = sum(variants)
        if number == 1:
            corners_count += 1
        elif number == 2:
            if variants == [True, False, True, False] or variants == [False, True, False, True]:
                corners_count += 2
        elif number == 3:
            corners_count += 1
    price += len(plant) * corners_count
print(price)
            
