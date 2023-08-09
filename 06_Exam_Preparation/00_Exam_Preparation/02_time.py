"""
exam: 02. Time
judge: https://judge.softuni.org/Contests/Practice/Index/3474#1

Solution using Longest common subsequence (LCS)
"""
from collections import deque


def reconstruct_timeline(dp):
    row = rows - 1
    col = cols - 1
    result = deque()

    while row > 0 and col > 0:
        if first_line[row - 1] == second_line[col - 1]:
            result.appendleft(first_line[row - 1])
            row -= 1
            col -= 1
        elif dp[row - 1][col] > dp[row][col - 1]:
            row -= 1
        else:
            col -= 1

    return result


first_line = [int(x) for x in input().split()]
second_line = [int(x) for x in input().split()]

rows = len(first_line) + 1
cols = len(second_line) + 1

dp = [[0] * cols for _ in range(rows)]

for row in range(1, rows):
    for col in range(1, cols):
        if first_line[row - 1] == second_line[col - 1]:
            dp[row][col] = dp[row - 1][col - 1] + 1
        else:
            dp[row][col] = max(dp[row][col - 1], dp[row - 1][col])

print(*reconstruct_timeline(dp))
print(dp[-1][-1])
