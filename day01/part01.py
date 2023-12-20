from sys import stdin

sum_of_caluclations = 0
for line in stdin:
    first = "-10"
    last = "-10"
    for char in line:
        if char.isdigit():
            if first == "-10":
                first = char
            last = char
    sum_of_caluclations += int(first+last)

print(sum_of_caluclations)