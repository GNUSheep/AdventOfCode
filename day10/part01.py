from sys import stdin

def point_returner(element, x, y):
    if element == "|":
        return [(x, y-1), (x, y+1)]  
    if element == "-":
        return [(x-1, y), (x+1, y)]
    if element == "L":
        return [(x, y-1), (x+1, y)]
    if element == "J":
        return [(x-1, y), (x, y-1)]
    if element == "7":
        return [(x-1, y), (x, y+1)]
    if element == "F":
        return [(x, y+1), (x+1, y)]

diagram = {}
y = 1
start_points = (0, 0)
for line in stdin:
    x = 1
    for element in line:
        if element != "." and element != "S" and element != "\n":
            diagram[x, y] = point_returner(element, x, y)
        if element == "S":
            start_points = (x, y)
        x += 1
    y += 1

routes = []
if (start_points[0]-1, start_points[1]) in diagram and start_points in diagram[(start_points[0]-1, start_points[1])]:
    routes.append([start_points[0]-1, start_points[1]])
#RIGHT
if (start_points[0]+1, start_points[1]) in diagram and start_points in diagram[(start_points[0]+1, start_points[1])]:
    routes.append([start_points[0]+1, start_points[1]])
# TOP
if (start_points[0], start_points[1]-1) in diagram and start_points in diagram[(start_points[0], start_points[1]-1)]:
    routes.append([start_points[0], start_points[1]-1])
# DOWN
if (start_points[0], start_points[1]+1) in diagram and start_points in diagram[(start_points[0], start_points[1]+1)]:
    routes.append([start_points[0], start_points[1]+1])

pos1 = start_points
pos2 = start_points
ways = 0

while routes[0] != routes[1]:
    for options in diagram[routes[0][0], routes[0][1]]:
        if options != pos1:
            pos1 = (routes[0][0], routes[0][1])
            routes[0] = options
            break

    for options in diagram[routes[1][0], routes[1][1]]:
        if options != pos2:
            pos2 = (routes[1][0], routes[1][1])
            routes[1] = options
            break
    ways += 1
print(ways+1)
