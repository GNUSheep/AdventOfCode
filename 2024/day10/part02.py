from sys import stdin

map = []
start_pos = []
for line in stdin:
    col = []
    for i in range(0, len(line.strip())):
        if line[i] == "0":
            start_pos.append((i, len(map)))
        col.append(int(line[i]))
    map.append(col)

sum_of_rating = 0
for pos in start_pos:
    moves = [(pos[0], pos[1])]
    while len(moves) != 0:
        move = moves.pop()

        if map[move[1]][move[0]] == 9:
            sum_of_rating += 1

        # up, down, left, right x y
        for dir in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            n_x = move[0] + dir[0]
            n_y = move[1] + dir[1]
        
            if not (0 <= n_x < len(map[0]) and 0 <= n_y < len(map)):
                continue

            if map[n_y][n_x] == map[move[1]][move[0]] + 1:
                moves.append((n_x, n_y))
print(sum_of_rating)
