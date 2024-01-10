from sys import stdin

seeds = [int(i) for i in input().split()[1:]]
_ = input() # skip newline

seeds_ranges = []
for i in range(0, len(seeds), 2):
    seeds_ranges.append([seeds[i], seeds[i]+seeds[i+1]])

def solve(seeds_arr, ranges):
    new_seeds = []

    while seeds_arr:
        rng_start, rng_end = seeds_arr.pop()
        for dst, src, rng in ranges:
            os = max(int(rng_start), int(src))
            oe = min(int(rng_end), int(src)+int(rng))
            if int(os) < int(oe):
                new_seeds.append([int(os)-int(src)+int(dst), int(oe)-int(src)+int(dst)])
                if int(os) > int(rng_start):
                    seeds_arr.append([int(rng_start), int(os)])
                if int(rng_end) > int(oe):
                    seeds_arr.append([int(oe), int(rng_end)])
                break
        else:
            new_seeds.append([int(rng_start), int(rng_end)])

    return new_seeds

## tried to do a line by line, but cannot get it working
seeds_r = seeds_ranges
ranges = []
for line in stdin:
    if "to" in line:
        continue 
    if "\n" == line:
        seeds_r = solve(seeds_r, ranges)
        ranges = []
        continue

    ranges.append(list(line.split()))

print(min(seeds_r)[0])