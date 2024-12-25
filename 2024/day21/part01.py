from sys import stdin
from itertools import permutations, product

numeric_keypad = {
    "7": (0, 0),
    "8": (1, 0),
    "9": (2, 0),
    "4": (0, 1),
    "5": (1, 1),
    "6": (2, 1),
    "1": (0, 2),
    "2": (1, 2),
    "3": (2, 2),
    "0": (1, 3),
    "A": (2, 3),
}

direction_keypad = {
    "^": (1, 0),
    "A": (2, 0),
    "<": (0, 1),
    "v": (1, 1),
    ">": (2, 1),
}

dir = {
    "<": (-1, 0),
    ">": (1, 0),
    "^": (0, -1),
    "v": (0, 1),
}

def gen_ways(code, keypad):
    pos = keypad["A"]

    ways = []
    for c in code:
        n_pos = keypad[c]

        moves = ""
        
        side_dir = ">" if n_pos[0] - pos[0] > 0 else "<"
        ud_dir = "v" if n_pos[1] - pos[1] > 0 else "^"

        moves = side_dir * abs(n_pos[0] - pos[0]) + ud_dir * abs(n_pos[1] - pos[1])
        
        raw_perm_ways = list(set(["".join(x) + "A" for x in permutations(moves)]))
        perms = []
        for way in raw_perm_ways:
            c_x, c_y = pos
            
            for move in way[:-1]:
                mv_x, mv_y = dir[move]
                c_x, c_y = c_x + mv_x, c_y + mv_y
                
                if not (c_x, c_y) in keypad.values():
                    break
            else:
                perms.append(way)    
        ways.append(perms)
        pos = n_pos
    
    return ["".join(x) for x in product(*ways)]

sum_of_complexities = 0    
for line in stdin:
    ways = gen_ways(line.strip(), numeric_keypad)
    for _ in range(0, 2):
        n_ways = []
        for way in ways:
            n_ways.extend(gen_ways(way, direction_keypad))
        ways = n_ways
    sum_of_complexities += int(line.strip()[:-1]) * min([len(way) for way in ways])
print(sum_of_complexities)
