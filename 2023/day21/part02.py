from sys import stdin
import numpy

garden_map = []
positions = set()
for line in stdin:
    if "S" in line:
        positions.add((line.index("S"), len(garden_map)))
    garden_map.append(list(line.rstrip()))

# y x 
values = []
for i in range(131*2+65):
    new = set()
    
    if i == 65 + ((i//131)*131):
        values.append((i//131, len(positions)))

    while positions:
        x, y = positions.pop()

        # check all dirs
        for y_new, x_new in ((0,1), (0,-1), (1,0), (-1,0)):
            x_pos = x+x_new
            y_pos = y+y_new

            # right expansion
            if x_pos >= len(garden_map[0]):
                x_pos -= (x_pos//len(garden_map[0]))*len(garden_map[0])
            
            #  down expansion
            if y_pos >= len(garden_map):
                y_pos -= (y_pos//len(garden_map))*len(garden_map)

            # left expansion
            if x_pos < 0:
                x_pos += -((x_pos//len(garden_map[0]))*len(garden_map[0]))

            if y_pos < 0:
                y_pos += -((y_pos//len(garden_map))*len(garden_map))

            if garden_map[y_pos][x_pos] == "." or garden_map[y_pos][x_pos] == "S":
                new.add((x+x_new, y+y_new))
    positions = new

values.append((2, len(positions)))
fit = numpy.polyfit(*zip(*values), 2)

print(round(numpy.polyval(fit, 202300)))