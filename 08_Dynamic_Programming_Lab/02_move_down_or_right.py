from collections import deque

rows = int(input())
cols = int(input())

matrix = []
calc_matrix = []

for _ in range(rows):
    matrix.append([int(x) for x in input().split()])
    calc_matrix.append([0] * cols)

calc_matrix[0][0] = matrix[0][0]

# base calc -> calc if we have 1 row matrix
for col in range(1, cols):
    calc_matrix[0][col] = calc_matrix[0][col - 1] + matrix[0][col]

# base calc -> calc if we have 1 col matrix
for row in range(1, rows):
    calc_matrix[row][0] = calc_matrix[row - 1][0] + matrix[row][0]

# calc for the remaining matrix
for row in range(1, rows):
    for col in range(1, cols):
        calc_matrix[row][col] = max(calc_matrix[row - 1][col], calc_matrix[row][col - 1]) + matrix[row][col]

row = rows - 1
col = cols - 1

result = deque()

while row > 0 and col > 0:
    result.appendleft([row, col])
    # check if upper calc is greater than left calc
    if calc_matrix[row][col - 1] >= calc_matrix[row - 1][col]:
        col -= 1
    else:
        row -= 1

# when col is 0, go to through all left rows
while row > 0:
    result.appendleft([row, col])
    row -= 1

# when row is 0, go to through all left cols
while col > 0:
    result.appendleft([row, col])
    col -= 1

# add to result from where we start (0, 0)
result.appendleft([0, 0])

print(*result, sep=' ')
