from sys import stdin
import re

robots = []
for line in stdin:
  px,py,vx,vy = [int(n) for n in re.findall(r'-?\d+', line.strip())]
 
  robots.append([px, py, vx, vy])

width = 101
height = 103

grid = [[0] * width for _ in range(0, height)]
for sec in range(100000):  
  for i in range(0, len(robots)):
    px,py,vx,vy = robots[i][0], robots[i][1], robots[i][2], robots[i][3]
    n_x = px + vx
    
    if n_x >= width:
      n_x -= width
    elif n_x < 0:
      n_x += width
    
    n_y = py + vy
    
    if n_y >= height:
      n_y -= height
    elif n_y < 0:
      n_y += height

    if grid[py][px] != 0:
      grid[py][px] -= 1

    robots[i][0] = n_x
    robots[i][1] = n_y
    
    px = n_x
    py = n_y
    
    grid[py][px] += 1

  print(20 * "=")
  print(sec)
  for r in grid:
    print(r)
    
    
