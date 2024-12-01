from sys import stdin

workflows = {}
for line in stdin:
    if line == "\n":
        break
    name, rules = line[:-2].split("{")
    workflows[name] = rules.split(",")


variables_map = {"x": 0, "m": 1, "a": 2, "s": 3}

total = 0
for test in stdin:
    test = test.rstrip()[1:-1]
    test_vals = [int(x[2:]) for x in test.split(",")]

    queue = ["in"]
    is_accepted = False
    while queue:
        name = queue.pop(0)

        if name == "R":
            break

        if name == "A":
            is_accepted = True
            break

        for rule in workflows[name]:
            if ":" not in rule and "A" in rule:
                is_accepted = True
                break
            if ":" not in rule:
                queue.append(rule)
                break
            
            variable = rule[0]
            operator = rule[1]
            value, where_to_go = rule[2:].split(":")

            if operator == ">":
                if test_vals[variables_map[variable]] > int(value):
                    queue.append(where_to_go)
                    break
            else:
                if test_vals[variables_map[variable]] < int(value):
                    queue.append(where_to_go)
                    break

    if is_accepted:
        total += sum(test_vals)
print(total)