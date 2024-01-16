from sys import stdin
from collections import deque

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

pulses = {"high": 0, "low": 0}
for _ in range(1000):
    queue = deque()
    queue.append(("broadcaster", 0))

    while queue:
        module_name, pulse = queue.popleft()
        if pulse == 0:
            pulses["low"] += 1
        else:
            pulses["high"] += 1

        if module_name not in modules:
            continue

        for name in modules[module_name][-1]:
            print(module_name, name, pulse)
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

print(pulses["high"]*pulses["low"])