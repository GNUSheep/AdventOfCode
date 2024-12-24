from sys import stdin
from collections import defaultdict
import re

gates = defaultdict(int)
for line in stdin:
    if line == "\n": break
    gate, value = [v for v in re.findall(r'([a-zA-Z]+\d+): (\d)', line.strip())[0]]
    gates[gate] = int(value)

pattern = r'([a-zA-Z0-9]+)\s+(AND|XOR|OR)\s+([a-zA-Z0-9]+)\s+->\s+([a-zA-Z0-9]+)'
operations = []
for line in stdin:
    operations.append([v for v in re.findall(pattern, line.strip())[0]])

while True:
    v = list(gates.values())[:]
    
    for gate1, operator, gate2, gate3 in operations:
        if operator == "AND":
            gates[gate3] = int(gates[gate1] and gates[gate2])  
        elif operator == "XOR":
            gates[gate3] = int(gates[gate1] != gates[gate2])
        else:
            gates[gate3] = int(gates[gate1] or gates[gate2])

    if v == list(gates.values()):
        break

gates_sort = sorted(list(gates.keys()), reverse=True)
bin_n = ""
for gate in gates_sort:
    if "z" == gate[0]:
        bin_n += str(gates[gate])
print(int(bin_n, 2))
