from sys import stdin

sum_of_ids = 0
for line in stdin:
    red = 0
    blue = 0
    green = 0
    is_real = True
    line += ";"
    line_split = line.split(":")
    game = line_split[1].split(" ")
    for x in range(0, len(game)):
        if "red" in game[x]:
            red += int(game[x-1])
        elif "blue" in game[x]:
            blue += int(game[x-1])
        elif "green" in game[x]:
            green += int(game[x-1])
    
        if ";" in game[x]:
            if red > 12 or blue > 14 or 13 < green:
                is_real = False
            red = 0
            blue = 0
            green = 0

    if is_real:
        sum_of_ids += int(line_split[0].split(" ")[1])

print(sum_of_ids)
