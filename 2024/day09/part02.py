disk_map_in = input().strip()

disk_map = []
k = 0
empty_space = []
for i in range(0, len(disk_map_in)):
    start = len(disk_map)
    for j in range(0, int(disk_map_in[i])):
        if i % 2 == 0:
            disk_map.append(str(k))
        else:
            disk_map.append(".")
    if i % 2 == 0:
        k += 1
    else:
        empty_space.append((start, start+int(disk_map_in[i])))

end = len(disk_map) - 1
start = end
while end >= 0:
    c = disk_map[start]

    while c == disk_map[start]:
        start -= 1
    l = end - start
    if c != ".":
        b = 0
        e = 0
        while b < start:
            if disk_map[b] == ".":
                e = b
                while disk_map[e] == ".":
                    e += 1

                if e - b >= l:
                    break
            b += 1

        if e - b < l:
            end = start
            continue

        for i in range(b, b+l):
            disk_map[i] = c

        for i in range(start+1, end+1):
            disk_map[i] = "."       
    end = start

checksum = 0
for i in range(0, len(disk_map)):
    if disk_map[i] == ".":
        continue

    checksum += int(disk_map[i]) * i
print(checksum)
