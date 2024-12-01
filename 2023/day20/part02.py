from sys import stdin
from collections import deque
import math

modules = {}
for line in stdin:
    name, connections = line.strip().split("->")
    if name[0] in "&":
        modules[name[1:].strip()] = [name[0], {}, [con.strip() for con in connections.split(',')]]
    elif name[0] in "%":
        modules[name[1:].strip()] = [name[0], "off", [con.strip() for con in connections.split(',')]]
    else:
        modules[name.strip()] = ["", 0, [con.strip() for con in connections.split(',')]]

for mod in modules:
    if modules[mod][0] == "&":
        for con in modules:
            if mod in modules[con][2]:
                modules[mod][1][con] = 0

# solution idea from hyper-neutrino
(feed,) = [name for name, module in modules.items() if "rx" in module[2]]
cycle_lengths = {}
seen = {name: 0 for name, module in modules.items() if feed in module[2]}
presses = 0

queue = deque()
while True:
    presses += 1
    queue.append(("broadcaster", 0))

    while queue:
        module_name, pulse = queue.popleft()

        if module_name not in modules:
            continue

        for name in modules[module_name][-1]:
            if feed == name and pulse == 0:
                seen[module_name] += 1

                if module_name not in cycle_lengths:
                    cycle_lengths[module_name] = presses
                else:
                    assert presses == seen[module_name] * cycle_lengths[module_name]

                if all(seen.values()):
                    x = 1
                    for cycle_length in cycle_lengths.values():
                        x = math.lcm(x, cycle_length)
                    print(x)
                    exit(0)


            if modules[module_name][0] == "%":
                if pulse == 1:
                    continue

                if modules[module_name][1] == "off":
                    if name in modules and modules[name][0] == "&":
                        modules[name][1][module_name] = 1
                    queue.append((name, 1))
                else:
                    if name in modules and modules[name][0] == "&":
                        modules[name][1][module_name] = 0
                    queue.append((name, 0))

            elif modules[module_name][0] == "&":
                isHigh = True

                for val in modules[module_name][1].values():
                    if val != 1:
                        isHigh = False
                        break

                if name in modules and modules[name][0] == "&":
                    modules[name][1][module_name] = int(not isHigh)
                queue.append((name, int(not isHigh)))
            else:
                if name in modules and modules[name][0] == "&":
                    modules[name][1][module_name] = pulse
                queue.append((name, pulse))

        if modules[module_name][0] == "%" and pulse != 1: 
            if modules[module_name][1] == "off":
                modules[module_name][1] = "on"
            else:
                modules[module_name][1] = "off"