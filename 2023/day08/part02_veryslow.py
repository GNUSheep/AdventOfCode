from sys import stdin

lr_instructions = input()
nodes = {}
for line in stdin:
    if line != "\n":
        line = line.split()
        src = line[0]
        l_dst = line[2][1:len(line[2])-1]
        r_dst = line[3][:len(line[3])-1]

        nodes[src] = [l_dst, r_dst]


cur_nodes = []
for node in nodes.keys():
    if "A" in node:
        cur_nodes.append(node)

def is_all_z():
    for node in cur_nodes:
        if "Z" not in node:
            return False
    return True

direction = 0
ways = 0
while not is_all_z():
    cur_dir = 0
    if lr_instructions[direction] == "R":
        cur_dir = 1

    for i in range(0, len(cur_nodes)):
        cur_nodes[i] = nodes[cur_nodes[i]][cur_dir]
    
    ways += 1

    direction += 1
    if direction == len(lr_instructions):
        direction = 0
print(ways)