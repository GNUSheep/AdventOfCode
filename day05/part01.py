from sys import stdin

seeds = [[int(i), False] for i in input().split()[1:]]
_ = input() # skip newline

for line in stdin:
    if "to" in line:
        continue 
    if "\n" == line:
        for index in range(len(seeds)):
            seeds[index][1] = False
        continue
    
    dst, src, rng = line.split()
    for index in range(len(seeds)):
        if int(src) <= seeds[index][0] <= int(src)+(int(rng)-1) and seeds[index][1] != True:
            if int(src) == seeds[index][0]:
                seeds[index][0] = int(dst)
            else:
                seeds[index][0] += int(dst) - int(src)
            seeds[index][1] = True
            
print(min(seeds)[0])