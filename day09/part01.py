from sys import stdin

sum_of_extrapolate = 0
for line in stdin:
    y = line.split()
    y = [eval(i) for i in y]
    
    diffs_all = [y[-1]]
    while diffs_all[-1] != 0:
        diff = []
        for i in range(0, len(y)-1):
            diff.append(y[i+1] - y[i])
        y = diff
        diffs_all.append(diff[-1])
    
    sum_of_extrapolate += sum(diffs_all)
print(sum_of_extrapolate)