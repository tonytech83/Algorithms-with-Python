first_str = input()
second_srt = input()

dp = []

rows = len(first_str) + 1
cols = len(second_srt) + 1

for _ in range(rows):
    dp.append([0] * cols)

# add base solutions for cols
for col in range(1, cols):
    dp[0][col] = col

# add  base solutions for rows
for row in range(1, rows):
    dp[row][0] = row

for row in range(1, rows):
    for col in range(1, cols):
        # check for coincidence
        if first_str[row - 1] == second_srt[col - 1]:
            # select upper left diagonal
            dp[row][col] = dp[row - 1][col - 1]
        # if they are not the same, select min result from left or upper cell
        else:
            dp[row][col] = min(dp[row][col - 1], dp[row - 1][col]) + 1

print(f'Deletions and Insertions: {dp[rows - 1][cols - 1]}')
