from sys import stdin
from collections import defaultdict

networks = defaultdict(list)

for line in stdin:
    n1, n2 = line.strip().split("-")

    networks[n1].append(n2)
    networks[n2].append(n1)

lan_party_max = []
def backtrack(lan_party, graph):
    global lan_party_max
    
    if len(lan_party) > len(lan_party_max):
        lan_party_max = lan_party[:]
    
    for i in range(len(graph)):
        node = graph[i]
            
        if all(lan in networks[node] for lan in lan_party):
            backtrack(lan_party + [node], graph[i + 1:])

backtrack([], list(networks.keys()))
print(",".join(sorted(lan_party_max)))
