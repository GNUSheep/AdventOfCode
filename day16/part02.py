from sys import stdin

grid = []
for line in stdin:
    grid.append(tuple(line.rstrip()))

def energize_grid(startpos):
    paths = [startpos]
    energized = set()
    while paths:
        row, col, direction = paths.pop(0)
        if direction == "r":
            col += 1
        elif direction == "l":
            col -= 1
        elif direction == "u":
            row -= 1
        elif direction == "d":
            row += 1
        
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
            continue
        
        if grid[row][col] == "." or (grid[row][col] == "-" and direction in "lr") or (grid[row][col] == "|" and direction in "ud"):
            paths.append((row, col, direction))
            energized.add((row, col, direction))
        elif grid[row][col] == "/":
            new_path = ()
            if direction == "r":
                new_path = (row, col, "u")
            elif direction == "l":
                new_path = (row, col, "d")
            elif direction == "u":
                new_path = (row, col, "r")
            else:
                new_path = (row, col, "l")

            if new_path not in energized:
                paths.append(new_path)
                energized.add(new_path)
        elif grid[row][col] == "\\":
            new_path = ()
            if direction == "r":
                new_path = (row, col, "d")
            elif direction == "l":
                new_path = (row, col, "u")
            elif direction == "u":
                new_path = (row, col, "l")
            else:
                new_path = (row, col, "r")

            if new_path not in energized:
                paths.append(new_path)
                energized.add(new_path)
        else:
            if grid[row][col] == "|":
                path = (row, col, "u")
                if path not in energized:
                    paths.append(path)
                    energized.add(path)
                path = (row, col, "d")
                if path not in energized:
                    paths.append(path)
                    energized.add(path)
            else:
                path = (row, col, "l")
                if path not in energized:
                    paths.append(path)
                    energized.add(path)
                path = (row, col, "r")
                if path not in energized:
                    paths.append(path)
                    energized.add(path)
    return len(set((row, col) for (row, col, _) in energized))

energized_count = 0
for row in range(0, len(grid)):
    energized_count = max(energize_grid((row, -1, "r")), energize_grid((row, len(grid[0]), "l")), energized_count)

for col in range(0, len(grid[0])):
    energized_count = max(energize_grid((-1, col, "d")), energize_grid((len(grid), col, "u")), energized_count)
print(energized_count)