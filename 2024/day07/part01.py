from sys import stdin

def backtrack(equations, test_value, current_value, i):
    if i == len(equations):
        return current_value == test_value

    if backtrack(equations, test_value, current_value + equations[i], i+1):
        return True

    if backtrack(equations, test_value, current_value * equations[i], i+1):
        return True

    return False
    
result = 0
for line in stdin:
    line_splitted = line.split()

    test_value = int(line_splitted[0][:-1])
    equations = [int(n) for n in line_splitted[1:]]

    if backtrack(equations, test_value, 0, 0):
        result += test_value
print(result)  
    
