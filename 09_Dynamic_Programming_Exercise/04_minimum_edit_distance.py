# looks like exam 2 -> Word differences

replace = int(input())
insert = int(input())
delete = int(input())

first_str = input()
second_str = input()

rows = len(first_str) + 1
cols = len(second_str) + 1

dp = []
for _ in range(rows):
    dp.append([0] * cols)

# fill base solutions for cols
for col in range(1, cols):
    dp[0][col] = dp[0][col - 1] + insert

# fill base solutions for rows
for row in range(1, rows):
    dp[row][0] = dp[row - 1][0] + delete

for row in range(1, rows):
    for col in range(1, cols):
        if first_str[row - 1] == second_str[col - 1]:
            dp[row][col] = dp[row - 1][col - 1]
        else:
            dp[row][col] = min(dp[row][col - 1] + insert, dp[row - 1][col] + delete, dp[row - 1][col - 1] + replace)

print(f'Minimum edit distance: {dp[rows - 1][cols - 1]}')
