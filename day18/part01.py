from sys import stdin
import math

def calculate_area(points):
    area = 0
    for i in range(0, len(points) - 1):
        area += (points[i][0]*points[i+1][1]) - (points[i+1][0]*points[i][1])
    return area/2 

points = [(0,0)]
for line in stdin:
    direction = line.split()[0]
    num_of_meters = int(line.split()[1])

    if direction == "R":
        for i in range(num_of_meters):
            points.append((points[-1][0]+1, points[-1][1]))
    elif direction == "L":
        for i in range(num_of_meters):
            points.append((points[-1][0]-1, points[-1][1]))
    elif direction == "U":
        for i in range(num_of_meters):
            points.append((points[-1][0], points[-1][1]-1))
    else:
        for i in range(num_of_meters):
            points.append((points[-1][0], points[-1][1]+1))

area = calculate_area(points)
inside_points = math.ceil(abs(area) - (len(points)/2) + 1)
print(inside_points + len(points) - 1)