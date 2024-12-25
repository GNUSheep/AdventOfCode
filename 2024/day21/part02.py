from sys import stdin
from itertools import permutations, product
from functools import lru_cache
    
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

@lru_cache(None)
def gen_ways(a, b, keypad):
    keypad = direction_keypad if keypad else numeric_keypad
    
    pos = keypad[a]
    n_pos = keypad[b]

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
    
    return perms 

@lru_cache(None)
def get_cost(a, b, keypad, depth):
    if depth == 0:
        return min([len(x) for x in gen_ways(a, b, True)])

    ways = gen_ways(a, b, keypad)
    best_cost = 10**1000
    for way in ways:
        way = "A" + way
        cost = 0

        for i in range(0, len(way) - 1):
            a, b = way[i], way[i+1]
            cost += get_cost(a, b, True, depth - 1)
        
        best_cost = min(best_cost, cost)

    return best_cost

def get_code_cost(code, depth):
    code = "A" + code
    cost = 0

    for i in range(0, len(code) - 1):
        a, b = code[i], code[i+1]
        cost += get_cost(a, b, False, depth)
    return cost

sum_of_complexities = 0    
for line in stdin:
    sum_of_complexities += get_code_cost(line.strip(), 25) * int(line.strip()[:-1])
print(sum_of_complexities)
