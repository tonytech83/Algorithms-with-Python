"""
exam: 02. Word Differences
judge: https://judge.softuni.org/Contests/Compete/Index/3473#1
"""

first = input()
second = input()

rows = len(first) + 1
cols = len(second) + 1

dp = [[0] * cols for _ in range(rows)]

# add  base solutions for rows
for row in range(1, rows):
    dp[row][0] = row

# add base solutions for cols
for col in range(1, cols):
    dp[0][col] = col

for row in range(1, rows):
    for col in range(1, cols):
        # check for coincidence, if True select upper left diagonal
        if first[row - 1] == second[col - 1]:
            dp[row][col] = dp[row - 1][col - 1]
        # if they are not the same, select min result from left or upper cell
        else:
            dp[row][col] = min(dp[row - 1][col], dp[row][col - 1]) + 1

print(f'Deletions and Insertions: {dp[-1][-1]}')
