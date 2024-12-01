from sys import stdin

sum_of_powers = 0
for line in stdin:
    red = 0
    red_max = 0

    blue = 0
    blue_max = 0

    green = 0
    green_max = 0

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
            red_max = max(red_max, red)
            blue_max = max(blue_max, blue)
            green_max = max(green_max, green)

            red = 0
            blue = 0
            green = 0
    sum_of_powers += red_max*blue_max*green_max
print(sum_of_powers)
