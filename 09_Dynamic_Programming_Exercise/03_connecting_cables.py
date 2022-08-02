# using Longest Common Subsequence - LCS

side_a = [int(x) for x in input().split()]
size = len(side_a) + 1

side_b = [cable for cable in range(1, size)]

lcs = []
[lcs.append([0] * size) for _ in range(size)]

for row in range(1, size):
    for col in range(1, size):
        if side_a[row - 1] == side_b[col - 1]:
            lcs[row][col] = lcs[row - 1][col - 1] + 1
        else:
            lcs[row][col] = max(lcs[row - 1][col], lcs[row][col - 1])

print(f'Maximum pairs connected: {lcs[size - 1][size - 1]}')
