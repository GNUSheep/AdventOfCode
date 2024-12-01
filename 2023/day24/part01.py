from sys import stdin

# a = vy
# b = -vx
# c = vy * x - vx * y

# x y z vx vy vz a b c
hailstones = []
for line in stdin:
    line = line.replace("@", ",")
    line = [i.strip() for i in line.split(',')]
    line = [eval(i) for i in line]
    hailstones.append({ "x": line[0], "y": line[1], "z": line[2], 
                        "vx": line[3], "vy": line[4], "vz": line[5], 
                        "a": line[4], "b": -line[3], "c": line[4]*line[0] - line[3]*line[1]})

how_many_cross = 0
for i, h1 in enumerate(hailstones):
    for _, h2 in enumerate(hailstones[:i]):
        if h1["a"] * h2["b"] == h1["b"] * h2["a"]:
            continue
        
        x = (h1["c"] * h2["b"] - h2["c"] * h1["b"]) / (h1["a"] * h2["b"] - h2["a"] * h1["b"])
        y = (h2["c"] * h1["a"] - h1["c"] * h2["a"]) / (h1["a"] * h2["b"] - h2["a"] * h1["b"] )
        if 200000000000000 <= x <= 400000000000000 and 200000000000000 <= y <= 400000000000000:
            if (x - h1["x"]) * h1["vx"] >= 0 and (y - h1["y"]) * h1["vy"] >= 0:
                if (x - h2["x"]) * h2["vx"] >= 0 and (y - h2["y"]) * h2["vy"] >= 0:
                    how_many_cross += 1
print(how_many_cross)