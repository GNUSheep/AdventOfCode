from sys import stdin
from itertools import combinations

def add_column(arr, index):
    for row in arr:
        row.insert(index, ".")


sky_map = []
for line in stdin:
    sky_map.append(list(line))
    if "#" not in line:
        sky_map.append(list(line))

empty_col = []
for i in range(0, len(sky_map[0])-1):
    columns = [j[i] for j in sky_map]
    if "#" not in columns:
        empty_col.append(i+len(empty_col))


for col in empty_col:
    add_column(sky_map, col)
 
galaxies = {}
galaxy_index = 1
for i in range(0, len(sky_map)):
    for j in range(0, len(sky_map[0])):
        if sky_map[i][j] == "#":
            galaxies[galaxy_index] = [i, j]
            galaxy_index += 1

galaxy_pairs = list(combinations([key for key in galaxies.keys()], 2))
sum_of_shortest_paths = 0
for pair in galaxy_pairs:
    x = abs(galaxies[pair[0]][0] - galaxies[pair[1]][0])
    y = abs(galaxies[pair[0]][1] - galaxies[pair[1]][1])
    sum_of_shortest_paths += x+y
print(sum_of_shortest_paths)
