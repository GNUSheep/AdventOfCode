from sys import stdin

workflows = {}
for line in stdin:
    if line == "\n":
        break
    name, rules = line[:-2].split("{")
    workflows[name] = rules.split(",")

def solve(variables, where_to_go):
    if where_to_go == "R":
        return 0

    if where_to_go == "A":
        combinations = 1
        for min_, max_ in variables.values():
            combinations *= max_ - min_ + 1
        return combinations

    last_rule = workflows[where_to_go][-1]
    combinations_count = 0
    for rule in workflows[where_to_go][:-1]:
        variable = rule[0]
        operator = rule[1]
        value, where_to_go = rule[2:].split(":")

        if operator == "<":
            passed = (variables[variable][0], int(value) - 1)
            n_passed = (int(value), variables[variable][1])
        else:
            passed = (int(value) + 1, variables[variable][1])
            n_passed = (variables[variable][0], int(value))
        
        if passed[0] <= passed[1]:
            passed_variables_values = dict(variables)
            passed_variables_values[variable] = passed
            combinations_count += solve(passed_variables_values, where_to_go)
        if n_passed[0] <= n_passed[1]:
            variables = dict(variables)
            variables[variable] = n_passed
        else:
            break
    else:
        combinations_count += solve(variables, last_rule)

    return combinations_count

print(solve({variable: (1, 4000) for variable in "xmas"}, "in"))