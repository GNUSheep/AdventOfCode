from sys import stdin

def solve(n):
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
    return n
secrets = []
for line in stdin:
    secrets.append(solve(int(line.strip())))
print(sum(secrets))
