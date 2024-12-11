from collections import defaultdict

line = input()
stones = defaultdict(int)
for stone in line.strip().split():
    stones[stone] = 1

for i in range(0, 25):
    new_stones = defaultdict(int)
    for (key,value) in stones.items():
        if key == "0":
            new_stones["1"] += value
        elif len(key) % 2 == 0:
            left = int(key[:len(key)//2])
            right = int(key[len(key)//2:])

            new_stones[str(left)] += value
            new_stones[str(right)] += value
        else:
            new_stones[str(2024 * int(key))] += value
    stones = new_stones

numbers_of_stones = sum([value for value in stones.values()])
print(numbers_of_stones)
