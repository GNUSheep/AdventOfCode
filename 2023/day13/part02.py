from sys import stdin

def solve(pattern):
    for col in range(1, len(pattern[0])):
        reflection_split = min(col, len(pattern[0]) - col)
        num_of_diffs = 0
        for row in pattern:
            for x, y in zip(row[col-reflection_split:col], row[col:col+reflection_split][::-1]):
                if x != y:
                    num_of_diffs += 1
        if num_of_diffs == 1:
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

