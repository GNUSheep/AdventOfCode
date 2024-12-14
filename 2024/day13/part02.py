from sys import stdin
from sympy import symbols, Eq, solve, simplify
    
machines = []
lines = stdin.read().strip().splitlines()
for i in range(0, len(lines), 4):
    btn_a = lines[i].split()
    a_x = int(btn_a[2][2:-1])
    a_y = int(btn_a[3][2:])
    
    btn_b = lines[i+1].split()
    b_x = int(btn_b[2][2:-1])
    b_y = int(btn_b[3][2:])
    
    prize = lines[i+2].split()
    prize_x = int(prize[1][2:-1]) + 10000000000000
    prize_y = int(prize[2][2:]) + 10000000000000
    machines.append([a_x, b_x, a_y, b_y, prize_x, prize_y])

x,y = symbols('x y')
prize = 0
for machine in machines:
    eq1 = Eq(machine[0]*x + machine[1]*y, machine[4])
    eq2 = Eq(machine[2]*x + machine[3]*y, machine[5])

    solution = solve((eq1, eq2), (x, y))
    if simplify(solution[x]).is_integer and simplify(solution[y]).is_integer:
        prize += (solution[x] * 3 + solution[y] * 1)
print(prize)
