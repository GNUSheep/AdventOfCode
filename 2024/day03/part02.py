from sys import stdin
import re

result = 0
for line in stdin:
    mul_extracted = re.findall("don't\(\)|do\(\)|mul\(\d+,\d+\)", line)

    enabled = True
    for instr in mul_extracted:
        if instr == "don't()":
            enabled = False
        elif instr == "do()":
            enabled = True
        elif enabled:
            n1, n2 = instr[4:len(instr) - 1].split(",")

            result += int(n1) * int(n2)
print(result)
