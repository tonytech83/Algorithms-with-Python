"""
exam: 03. Longest Common Subsequence
judge: https://judge.softuni.org/Contests/Practice/Index/3471#2

Finding the longest common subsequence (LCS) in given two sequences x[1...m] and y[1...n]
"""
from collections import deque

first = input()
second = input()
rows = len(first) + 1
cols = len(second) + 1

# generates matrix with all base cases (all zeros)
dp = [[0] * cols for _ in range(rows)]

for row in range(1, rows):
    for col in range(1, cols):
        if first[row - 1] == second[col - 1]:
            # if we have coincidence, should add upper-left diagonal cell + 1
            dp[row][col] = dp[row - 1][col - 1] + 1
        else:
            # when we haven't coincidence, better from previous left or upper cell as result
            dp[row][col] = max(dp[row][col - 1], dp[row - 1][col])

print(dp[-1][-1])

# Reconstruct the path
row = rows - 1
col = cols - 1
result = deque()

while row > 0 and col > 0:
    if first[row - 1] == second[col - 1]:
        result.appendleft(first[row - 1])  # same as second[col -1]
        row -= 1
        col -= 1
    elif dp[row - 1][col] > dp[row][col - 1]:
        row -= 1
    else:
        col -= 1

print(*result)