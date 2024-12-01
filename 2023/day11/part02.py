from sys import stdin
from itertools import combinations


sky_map = []
empty_rows = []
index = 0
for line in stdin:
    sky_map.append(list(line))
    if "#" not in line:
        empty_rows.append(index)
    index += 1

empty_col = []
for i in range(0, len(sky_map[0])-1):
    columns = [j[i] for j in sky_map]
    if "#" not in columns:
        empty_col.append(i)

galaxies = {}
galaxy_index = 1
for i in range(0, len(sky_map)):
    for j in range(0, len(sky_map[0])):
        if sky_map[i][j] == "#":
            galaxies[galaxy_index] = [i, j]
            galaxy_index += 1

galaxy_pairs = list(combinations([key for key in galaxies.keys()], 2))
#galaxy_pairs = [(1,7)]
sum_of_shortest_paths = 0
for pair in galaxy_pairs:
    x = abs(galaxies[pair[0]][0] - galaxies[pair[1]][0])
    y = abs(galaxies[pair[0]][1] - galaxies[pair[1]][1])
    dist =  x+y

    for x in range(min(galaxies[pair[0]][0], galaxies[pair[1]][0]), max(galaxies[pair[0]][0], galaxies[pair[1]][0])):
        if x in empty_rows:
            dist += 1000000 - 1
    
    for y in range(min(galaxies[pair[0]][1], galaxies[pair[1]][1]), max(galaxies[pair[0]][1], galaxies[pair[1]][1])):
        if y in empty_col:
            dist += 1000000 - 1
    
    sum_of_shortest_paths += dist

print(sum_of_shortest_paths)
