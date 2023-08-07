"""
exam: 02. Move Down/Right
judge: https://judge.softuni.org/Contests/Practice/Index/3471#1

Finding the longest sum in matrix of numbers
"""
from collections import deque

rows = int(input())
cols = int(input())

# create matrix form input
matrix = [[int(x) for x in input().split()] for _ in range(rows)]

# create sum matrix (dp) whit same size as matrix filled with 0
dp = [[0] * cols for _ in range(rows)]

# base cals 1 -> add sum of first element of matrix in sum matrix
dp[0][0] = matrix[0][0]

# base calc 2 -> calc if we have 1 row matrix
for col in range(1, cols):
    dp[0][col] = dp[0][col - 1] + matrix[0][col]

# base calc 3 -> calc if we have 1 col matrix
for row in range(1, rows):
    dp[row][0] = dp[row - 1][0] + matrix[row][0]

# fill the sums in remaining cells in sum matrix (dp)
for row in range(1, rows):
    for col in range(1, cols):
        dp[row][col] = max(dp[row - 1][col], dp[row][col - 1]) + matrix[row][col]

row = rows - 1
col = cols - 1
# keeps the indexes for each cell from sum matrix (dp)
result = deque()

while row > 0 and col > 0:
    result.appendleft([row, col])

    # there may have cases when we should prioritize left before up in matrix with equal cells
    if dp[row - 1][col] > dp[row][col - 1]:
        row -= 1
    else:
        col -= 1

# when col is 0, go to through all left rows
for idx in range(row, 0, -1):
    result.appendleft([idx, col])

# when row is 0, go to through all left cols
for idx in range(col, 0, -1):
    result.appendleft([row, idx])

result.appendleft([0, 0])

print(*result, sep=' ')
