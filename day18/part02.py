from sys import stdin
import math

last_points = (0,0)
area = 0
points_number = 1
for line in stdin:
    hex_encoded = line.split()[2]

    direction = hex_encoded[-2]
    num_of_meters = int("0x" + hex_encoded[2:-2], 16)

    if direction == "0":
        for i in range(num_of_meters):
            area += (last_points[0] * last_points[1]) - ((last_points[0]+1) * last_points[1])
            last_points = (last_points[0]+1, last_points[1])
            points_number += 1
    elif direction == "2":
        for i in range(num_of_meters):
            area += (last_points[0] * last_points[1]) - ((last_points[0]-1) * last_points[1])
            last_points = (last_points[0]-1, last_points[1])
            points_number += 1 
    elif direction == "3":
        for i in range(num_of_meters):
            area += (last_points[0] * (last_points[1]-1)) - (last_points[0] * last_points[1])
            last_points = (last_points[0], last_points[1]-1)
            points_number += 1
    else:
        for i in range(num_of_meters):
            area += (last_points[0] * (last_points[1]+1)) - (last_points[0] * last_points[1])
            last_points = (last_points[0], last_points[1]+1)
            points_number += 1

inside_points = math.ceil(abs(area/2) - (points_number/2) + 1)
print(inside_points + points_number - 1)