from sys import stdin

sum_of_extrapolate = 0
for line in stdin:
    y = line.split()
    y = [eval(i) for i in y]
    
    diffs_all = [y[0]]
    diff = [1] # tmp value 
    while any(diff):
        diff = []
        for i in reversed(range(1, len(y))):
            diff.append(y[-i] - y[-(i+1)])
        y = diff
        diffs_all.append(diff[0])

    sub_of_diffs = 0
    for diff in reversed(diffs_all):
        sub_of_diffs = diff - sub_of_diffs
    sum_of_extrapolate += sub_of_diffs

print(sum_of_extrapolate)
