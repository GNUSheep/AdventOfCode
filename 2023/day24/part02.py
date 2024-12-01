from sys import stdin
import sympy

# x y z vx vy vz
hailstones = []
for line in stdin:
    line = line.replace("@", ",")
    line = [i.strip() for i in line.split(',')]
    line = [eval(i) for i in line]
    hailstones.append(line)

rx, ry, rz, vrx, vry, vrz = sympy.symbols("rx, ry, rz, vrx, vry, vrz")

eq = []
for x, y, z, vx, vy, vz in hailstones:
    eq.append((rx - x) * (vy - vry) - (ry - y) * (vx - vrx))
    eq.append((ry - y) * (vz - vrz) - (rz - z) * (vy - vry))

answers = sympy.solve(eq)[0]
print(answers[rx] + answers[ry] + answers[rz])