sequences = input()
sequences = sequences.split(",")

total = 0
for seq in sequences:
    cur_value = 0
    for c in seq:
        cur_value += ord(c)
        cur_value *= 17
        cur_value %= 256
    total += cur_value
print(total)