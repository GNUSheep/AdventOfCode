from sys import stdin
from collections import defaultdict

grid = []
for line in stdin:
    grid.append([plant for plant in line.strip()])

# area, perimeter
seen = set()
plant_map = [] 
for y in range(0, len(grid)):
    for x in range(0, len(grid[0])): 
        moves = [(y, x)]
        plants = [0, 0]

        if (y,x) in seen:
            continue
        
        while len(moves) != 0:
            move = moves.pop()
            
            if (move[0], move[1]) in seen:
                continue
            seen.add((move[0], move[1]))
            
            plants[0] += 1

            # up, down, left, right y x
            for dir in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                n_y = move[0]+dir[0]
                n_x = move[1]+dir[1]

                if not (0 <= n_x < len(grid[0]) and (0 <= n_y < len(grid))):
                    plants[1] += 1  
                elif grid[n_y][n_x] != grid[y][x]:
                    plants[1] += 1

                if 0 <= n_x < len(grid[0]) and 0 <= n_y < len(grid):
                    if grid[n_y][n_x] == grid[move[0]][move[1]] and not ((n_y, n_x) in seen):
                        moves.append((n_y, n_x))
            # print(moves)
        if plants[0] != 0 and plants[1] != 0:
            plant_map.append(plants)
        
price = 0
for plant in plant_map:
    price += plant[0] * plant[1]
print(price)
