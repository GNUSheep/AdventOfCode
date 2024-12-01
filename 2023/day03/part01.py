from sys import stdin

engine_schematic = []

for line in stdin:
    engine_schematic.append(line.rstrip())

symbols = "[]\{\}|\\!@#$%^&*()_-+=;:'\"<>,/?`~"

sum_of_part_numbers = 0
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
                        sum_of_part_numbers += int(engine_schematic[row][start:end])
                        break
                    # RIGHT
                    if x+1 < len(engine_schematic[0]) and engine_schematic[row-1][x+1] in symbols:
                        sum_of_part_numbers += int(engine_schematic[row][start:end])
                        break
                    # TOP
                    if engine_schematic[row-1][x] in symbols:
                        sum_of_part_numbers += int(engine_schematic[row][start:end])
                        break

                # LEFT
                if x != 0 and engine_schematic[row][x-1] in symbols:
                    sum_of_part_numbers += int(engine_schematic[row][start:end])
                    break

                # RIGHT
                if x+1 < len(engine_schematic[0]) and engine_schematic[row][x+1] in symbols:
                    sum_of_part_numbers += int(engine_schematic[row][start:end])
                    break

                # DOWN
                if row < len(engine_schematic) - 1 :
                    # LEFT
                    if x != 0 and engine_schematic[row+1][x-1] in symbols:
                        sum_of_part_numbers += int(engine_schematic[row][start:end])
                        break
                    # RIGHT
                    if x+1 < len(engine_schematic[0]) and engine_schematic[row+1][x+1] in symbols:
                        sum_of_part_numbers += int(engine_schematic[row][start:end])
                        break
                    # TOP
                    if engine_schematic[row+1][x] in symbols:
                        sum_of_part_numbers += int(engine_schematic[row][start:end])
                        break        



            col = end
        col += 1

print(sum_of_part_numbers)
