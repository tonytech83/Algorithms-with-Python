"""
exam: 04. Minimum Edit Distance
judge: https://judge.softuni.org/Contests/Compete/Index/3473#3

solution with LCS
"""
replace_cost = int(input())
insert_cost = int(input())
delete_cost = int(input())

string_a = input()
string_b = input()

rows = len(string_a) + 1
cols = len(string_b) + 1

dp = [[0] * cols for _ in range(rows)]

# fill base solutions for cols
for col in range(1, cols):
    dp[0][col] = dp[0][col - 1] + insert_cost

# fill base solutions for rows
for row in range(1, rows):
    dp[row][0] = dp[row - 1][0] + delete_cost

for row in range(1, rows):
    for col in range(1, cols):
        if string_a[row - 1] == string_b[col - 1]:
            dp[row][col] = dp[row - 1][col - 1]
        else:
            insert = dp[row][col - 1] + insert_cost
            delete = dp[row - 1][col] + delete_cost
            replace = dp[row - 1][col - 1] + replace_cost

            dp[row][col] = min(insert, delete, replace)

print(f'Minimum edit distance: {dp[-1][-1]}')
