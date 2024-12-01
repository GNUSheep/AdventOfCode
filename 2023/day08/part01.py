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

cur_node = "AAA"
direction = 0
ways = 0
while cur_node != "ZZZ":
    cur_dir = 0
    if lr_instructions[direction] == "R":
        cur_dir = 1

    cur_node = nodes[cur_node][cur_dir]
    ways += 1

    direction += 1
    if direction == len(lr_instructions):
        direction = 0
print(ways)