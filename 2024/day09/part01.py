disk_map_in = input()

disk_map = []
k = 0
for i in range(0, len(disk_map_in)):
    for j in range(0, int(disk_map_in[i])):
        if i % 2 == 0:
            disk_map.append(str(k))
        else:
            disk_map.append(".")
    if i % 2 == 0:
        k += 1

b = 0
e = len(disk_map) - 1

while b != e:
    if disk_map[b] == ".":
        while disk_map[e] == ".":
            e -= 1
        if e <= b:
            break

        disk_map[b] = disk_map[e]
        disk_map[e] = "."
    b += 1

checksum = 0
for i in range(0, len(disk_map)):
    if disk_map[i] == ".":
        continue

    checksum += int(disk_map[i]) * i
print(checksum)
