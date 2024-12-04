from sys import stdin

grid = []
for line in stdin:
    line = line.strip()
    grid.append([c for c in line])

n = len(grid[0])
m = len(grid)

def searchWord(r, c):
    word = "XMAS"

    if grid[r][c] != word[0]:
        return 0

    # left, right, up, down, lu, ld, ru, rd
    dirs = ((-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1))

    xmas_count = 0
    for r_dir, c_dir in dirs:
        i_word = 1

        cR, cC = r + r_dir, c + c_dir

        while i_word < len(word):
            if not (0 <= cR < m) or not (0 <= cC < n):
                break

            if grid[cR][cC] != word[i_word]:
                break

            i_word += 1
            cR += r_dir
            cC += c_dir

        if i_word == len(word):
            xmas_count += 1

    return xmas_count
        
result = 0
for i in range(0, m):
    for j in range(0, n):
        result += searchWord(i, j)
print(result)
