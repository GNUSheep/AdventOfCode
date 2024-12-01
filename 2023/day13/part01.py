from sys import stdin

def solve(pattern):
    for col in range(1, len(pattern[0])):
        perfect_reflection = True
        reflection_split = min(col, len(pattern[0]) - col)
        for row in pattern:
            if row[col-reflection_split:col] != row[col:col+reflection_split][::-1]:
                perfect_reflection = False
                break
        if perfect_reflection:
            return col
    return 0

pattern = []
total = 0
for line in stdin:
    if line == "\n":
        total += solve(pattern)
        total += solve(list(zip(*pattern))) * 100
        pattern = []
    else:
        pattern.append(line.rstrip())
print(total)

