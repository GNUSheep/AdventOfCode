from sys import stdin

garden_map = []
positions = set()
for line in stdin:
    if "S" in line:
        positions.add((line.index("S"), len(garden_map)))
    garden_map.append(list(line.rstrip()))

# y x 
for _ in range(65):
    new = set()
    
    while positions:
        x, y = positions.pop()

        # check all dirs
        for y_new, x_new in ((0,1), (0,-1), (1,0), (-1,0)):
            if garden_map[y+y_new][x+x_new] == ".":
                new.add((x+x_new, y+y_new))
    positions = new

print(len(positions)+1)