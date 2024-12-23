from sys import stdin
from collections import defaultdict

networks = defaultdict(list)

for line in stdin:
    n1, n2 = line.strip().split("-")

    networks[n1].append(n2)
    networks[n2].append(n1)

# for (k, v) in networks.items():
    # print(k, v)

inter_sets = set()
for (k, v) in networks.items():
    for i in range(0, len(v)):
        for v1 in v:
            if v1 in networks[v[i]]:
                if "t" == v1[0] or "t" == k[0] or "t" == v[i][0]:
                    inter_sets.add(tuple(sorted((k, v[i], v1))))

print(len(inter_sets))
