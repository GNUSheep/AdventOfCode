from sys import stdin

def slide(platform):
    rotated_platform = []
    for row in platform:
        rotated_row = "".join(row)
        while ".O" in rotated_row:
            rotated_row = rotated_row.replace(".O", "O.")
        rotated_platform.append(tuple(rotated_row))
    
    return tuple(rotated_platform)


def solve(platform):
    total = 0
    for index, row in enumerate(platform):
        total += row.count("O") * (len(platform) - index)
    return total

platform = []
for line in stdin:
    platform.append(tuple(line.rstrip()))

platform = tuple(platform)

cache = {platform: 0}
seen_list = [platform]
for cycle in range(0, 1000000000):
    for turn in range(0, 4):
        platform = tuple(zip(*platform))
        platform = slide(platform)
        platform = tuple(zip(*platform))

        platform = tuple(zip(*platform[::-1]))
    
    if platform in cache:
        break
    cache[platform] = cycle + 1
    seen_list.append(platform)

spins = (1000000000 - seen_list.index(platform))
remaining_spins = (cycle + 1 - seen_list.index(platform))
index = spins % remaining_spins + seen_list.index(platform)

print(solve(seen_list[index]))