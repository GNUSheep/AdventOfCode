from sys import stdin
import re

registers = {"A": 0, "B": 0, "C": 0}
for line in stdin:
    if line == "\n": break
    
    regex = re.findall(r'([A-C]):\s(\d+)', line.strip())
    reg = regex[0][0]
    value = int(regex[0][1])
    
    registers[reg] = value

program = [int(prog) for prog in re.findall(r'Program:\s([\d,]+)', input().strip())[0].split(',')]

def get_operand(n):
    if operand == 4: return registers["A"]
    elif operand == 5: return registers["B"]
    elif operand == 6: return registers["C"]
    elif operand == 7: print("YU CATCH ME")
    
    return n

op_i = 0
registers[""]
while op_i < len(program):
     opcode = program[op_i]
     operand = program[op_i + 1]

     if opcode == 0:
         dividor = get_operand(operand)
     
         registers["A"] = registers["A"] // (2**dividor) 
     elif opcode == 1:
         registers["B"] = registers["B"] ^ operand
     elif opcode == 2:
         combo_operand = get_operand(operand)

         registers["B"] = combo_operand % 8
     elif opcode == 3 and registers["A"] != 0:        
         op_i = operand
         continue
     elif opcode == 4:
         registers["B"] = registers["B"] ^ registers["C"]
     elif opcode == 5:
         combo_operand = get_operand(operand)

         print(combo_operand % 8)   
     elif opcode == 6:
         dividor = get_operand(operand)
     
         registers["B"] = registers["A"] // (2**dividor)
     elif opcode == 7:
         dividor = get_operand(operand)
     
         registers["C"] = registers["A"] // (2**dividor)
      
     op_i += 2
       
