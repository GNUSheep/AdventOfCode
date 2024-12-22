from sys import stdin
from collections import defaultdict

def solve(n):
    secrets = [n % 10]
    for _ in range(0, 2000):
        result = n * 64
        n = result ^ n
        n %= 16777216

        result = n // 32
        n = result ^ n
        n %= 16777216

        result = n * 2048
        n = result ^ n
        n %= 16777216

        secrets.append(n%10)
    return secrets
    
sequences = defaultdict(int)
for line in stdin:
    secrets = solve(int(line.strip()))

    seen = set()
    for i in range(0, len(secrets) - 4):
        b1, b2, b3, b4, b5 = secrets[i:i+5]

        sequence = (b2 - b1, b3 - b2, b4 - b3, b5 - b4)

        if sequence in seen:
            continue
        seen.add(sequence)

        sequences[sequence] += b5
print(max(sequences.values()))
