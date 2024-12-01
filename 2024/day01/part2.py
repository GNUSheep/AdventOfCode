from sys import stdin

left = []
right = []
for line in stdin:
    l, r = line.split()

    left.append(int(l))
    right.append(int(r))

similarity_score = 0
for n in left:
    similarity_score += n * right.count(n)

print(similarity_score)
