from sys import stdin

towels = input().strip().split(", ")

c = 0
for line in stdin:
    if line == "\n": continue

    line = line.strip()
    
    letters = [0] * (len(line) + 1)
    letters[0] = 1 

    for i in range(1, len(line) + 1):
        for towel in towels:
            if line[i - len(towel):i] == towel and letters[i - len(towel)]:
                letters[i] += letters[i - len(towel)]
            
    c += letters[len(line)]
print(c)
