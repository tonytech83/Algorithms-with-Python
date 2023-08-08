"""
exam: 03. Connecting Cables
judge: https://judge.softuni.org/Contests/Compete/Index/3473#2

solution with LCS
"""
side_a = input().split()
side_b = list(sorted(side_a))

size = len(side_a) + 1

lcs = [[0] * size for _ in range(size)]

# Example:
# idx:      [0, 1, 2, 3, 4, 5, 6, 7, 8]
# side_a:   [2, 5, 3, 8, 7, 4, 6, 9, 1]
# side_b:   [1, 2, 3, 4, 5, 6, 7, 8, 9]

for row in range(1, size):
    for col in range(1, size):
        if side_a[row - 1] == side_b[col - 1]:
            lcs[row][col] = lcs[row - 1][col - 1] + 1
        else:
            lcs[row][col] = max(lcs[row][col - 1], lcs[row - 1][col])

print(f'Maximum pairs connected: {lcs[-1][-1]}')

# Result will be with LCS:
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 1, 1, 1, 1, 1, 1, 1, 1]
# [0, 0, 1, 1, 1, 2, 2, 2, 2, 2]
# [0, 0, 1, 2, 2, 2, 2, 2, 2, 2]
# [0, 0, 1, 2, 2, 2, 2, 2, 3, 3]
# [0, 0, 1, 2, 2, 2, 2, 3, 3, 3]
# [0, 0, 1, 2, 3, 3, 3, 3, 3, 3]
# [0, 0, 1, 2, 3, 3, 4, 4, 4, 4]
# [0, 0, 1, 2, 3, 3, 4, 4, 4, 5]
# [0, 1, 1, 2, 3, 3, 4, 4, 4, 5]
