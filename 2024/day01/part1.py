from sys import stdin

left = []
right = []
for line in stdin:
    l, r = line.split()

    left.append(int(l))
    right.append(int(r))

left.sort()
right.sort()

sum_of_distances = 0
for i in range(0, len(left)):
    sum_of_distances += abs(left[i] - right[i])
    
print(sum_of_distances)
