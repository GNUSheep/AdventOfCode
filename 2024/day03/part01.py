from sys import stdin
import re

result = 0
for line in stdin:
    mul_extracted = re.findall("mul\\(\\d{1,3},\\d{1,3}\\)", line)

    for instr in mul_extracted:
        n1, n2 = instr[4:len(instr) - 1].split(",")

        result += int(n1) * int(n2)
print(result)
