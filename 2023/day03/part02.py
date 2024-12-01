from sys import stdin

engine_schematic = []

for line in stdin:
    engine_schematic.append(line.rstrip())

symbols = "*"
gears_counter = {}
gear_ratio = {}
for row in range(0, len(engine_schematic)):
    col = 0
    while col < len(engine_schematic[0]):
        if engine_schematic[row][col].isdigit():
            start = col
            end = col

            while end < len(engine_schematic[0]) and engine_schematic[row][end].isdigit():
                end += 1

            for x in range(start, end):
                # TOP 
                if row != 0:
                    # LEFT
                    if x != 0 and engine_schematic[row-1][x-1] in symbols:
                        if (row-1, x-1) not in gears_counter.keys():
                            gears_counter[row-1, x-1] = 1
                            gear_ratio[row-1, x-1] = int(engine_schematic[row][start:end])
                        else:
                            gears_counter[row-1, x-1] += 1 
                            gear_ratio[row-1, x-1] *= int(engine_schematic[row][start:end])                        
                        break
                    # RIGHT
                    if x+1 < len(engine_schematic[0]) and engine_schematic[row-1][x+1] in symbols:
                        if (row-1, x+1) not in gears_counter.keys():
                            gears_counter[row-1, x+1] = 1
                            gear_ratio[row-1, x+1] = int(engine_schematic[row][start:end])
                        else:
                            gears_counter[row-1, x+1] += 1
                            gear_ratio[row-1, x+1] *= int(engine_schematic[row][start:end])                            
                        break
                    # TOP
                    if engine_schematic[row-1][x] in symbols:
                        if (row-1, x) not in gears_counter.keys():
                            gears_counter[row-1, x] = 1
                            gear_ratio[row-1, x] = int(engine_schematic[row][start:end]) 
                        else:
                            gears_counter[row-1, x] += 1
                            gear_ratio[row-1, x] *= int(engine_schematic[row][start:end])                             
                        break

                # LEFT
                if x != 0 and engine_schematic[row][x-1] in symbols:
                    if (row, x-1) not in gears_counter.keys():
                        gears_counter[row, x-1] = 1
                        gear_ratio[row, x-1] = int(engine_schematic[row][start:end])  
                    else:
                        gears_counter[row, x-1] += 1
                        gear_ratio[row, x-1] *= int(engine_schematic[row][start:end])  
                    break

                # RIGHT
                if x+1 < len(engine_schematic[0]) and engine_schematic[row][x+1] in symbols:
                    if (row, x+1) not in gears_counter.keys():
                        gears_counter[row, x+1] = 1
                        gear_ratio[row, x+1] = int(engine_schematic[row][start:end])  
                    else:
                        gears_counter[row, x+1] += 1
                        gear_ratio[row, x+1] *= int(engine_schematic[row][start:end])  
                    break

                # DOWN
                if row < len(engine_schematic) - 1 :
                    # LEFT
                    if x != 0 and engine_schematic[row+1][x-1] in symbols:
                        if (row+1, x-1) not in gears_counter.keys():
                            gears_counter[row+1, x-1] = 1
                            gear_ratio[row+1, x-1] = int(engine_schematic[row][start:end])  
                        else:
                            gears_counter[row+1, x-1] += 1
                            gear_ratio[row+1, x-1] *= int(engine_schematic[row][start:end])  
                        break
                    # RIGHT
                    if x+1 < len(engine_schematic[0]) and engine_schematic[row+1][x+1] in symbols:
                        if (row+1, x+1) not in gears_counter.keys():
                            gears_counter[row+1, x+1] = 1
                            gear_ratio[row+1, x+1] = int(engine_schematic[row][start:end])  
                        else:
                            gears_counter[row+1, x+1] += 1 
                            gear_ratio[row+1, x+1] *= int(engine_schematic[row][start:end])  
                        break
                    # TOP
                    if engine_schematic[row+1][x] in symbols:
                        if (row+1, x) not in gears_counter.keys():
                            gears_counter[row+1, x] = 1
                            gear_ratio[row+1, x] = int(engine_schematic[row][start:end])  
                        else:
                            gears_counter[row+1, x] += 1 
                            gear_ratio[row+1, x] *= int(engine_schematic[row][start:end])  
                        break    
            col = end
        col += 1

sum_of_gears_ratio = 0
proper_gears = {x for x in gears_counter if gears_counter[x] == 2}
for gear in proper_gears:
    sum_of_gears_ratio += gear_ratio[gear]
print(sum_of_gears_ratio)