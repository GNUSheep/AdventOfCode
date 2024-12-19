from sys import stdin
import re

registers = {"A": 0, "B": 0, "C": 0}
for line in stdin:
    if line == "\n": break
    
    regex = re.findall(r'([A-C]):\s(\d+)', line.strip())
    reg = regex[0][0]
    value = int(regex[0][1])
    
    registers[reg] = value

program_copy = [int(prog) for prog in re.findall(r'Program:\s([\d,]+)', input().strip())[0].split(',')]

def get_operand(n):
    if n == 4: return registers["A"]
    elif n == 5: return registers["B"]
    elif n == 6: return registers["C"]
    elif n == 7: print("YU CATCH ME")
    
    return n

def solve(a, b, c, program):
    op_i = 0
    values = []
    registers["A"] = a
    registers["B"] = b
    registers["C"] = c
    
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

            values.append(combo_operand % 8)
        elif opcode == 6:
            dividor = get_operand(operand)
        
            registers["B"] = registers["A"] // (2**dividor)
        elif opcode == 7:
            dividor = get_operand(operand)
        
            registers["C"] = registers["A"] // (2**dividor)
         
        op_i += 2
    return values

# help to  https://www.reddit.com/r/adventofcode/comments/1hg38ah/comment/m2gge90/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button       
def get_best_quine_input(program, cursor, value):
    for candidate in range(8):
        if solve(value * 8 + candidate, 0, 0, program) == program[cursor:]:
            if cursor == 0:
                return value * 8 + candidate
            ret = get_best_quine_input(program, cursor - 1, value * 8 + candidate)
            if ret is not None:
                return ret
    return None

print(get_best_quine_input(program_copy, len(program_copy) - 1, 0))
