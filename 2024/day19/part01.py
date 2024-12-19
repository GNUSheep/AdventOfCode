from sys import stdin

towels = input().strip().split(", ")

c = 0
for line in stdin:
    if line == "\n": continue

    line = line.strip()
    
    letters = [False] * (len(line) + 1)
    letters[0] = True

    for i in range(1, len(line) + 1):
        for towel in towels:
            if line[i - len(towel):i] == towel and letters[i-len(towel)]:
                letters[i] = True
                break
    if letters[len(line)]:
        c += 1
print(c)
