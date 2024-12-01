from sys import stdin

sum_of_caluclations = 0
for line in stdin:
    line = line.replace("one", "o1e")
    line = line.replace("two", "t2o")
    line = line.replace("three", "t3e")
    line = line.replace("four", "f4r")
    line = line.replace("five", "f5e")
    line = line.replace("six", "s6x")
    line = line.replace("seven", "s7n")
    line = line.replace("eight", "e8t")
    line = line.replace("nine", "n9e")

    first = "-10"
    last = "-10"
    for char in line:
        if char.isdigit():
            if first == "-10":
                first = char
            last = char
    sum_of_caluclations += int(first+last)

print(sum_of_caluclations)