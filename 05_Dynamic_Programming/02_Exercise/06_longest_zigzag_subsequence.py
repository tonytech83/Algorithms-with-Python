"""
exam: 06. Longest Zigzag Subsequence
judge: https://judge.softuni.org/Contests/Compete/Index/3473#5

solution with LIS
"""
from collections import deque

# Example size matrix:
# 	8	3	5	7
# <	1	1	3	3
# >	1	2	2	2

# Example parent matrix:
# 	  8	      3	    5	7
# <	None	None	1	1
# >	None	 0	    0	0


nums = [int(x) for x in input().split()]

dp = [[0] * len(nums) for _ in range(2)]
parent = [[None] * len(nums) for _ in range(2)]

# base case
dp[0][0] = dp[1][0] = 1

best_size = 0
best_row = 0
best_col = 0

for current_idx in range(1, len(nums)):
    current_number = nums[current_idx]
    current_size = 1

    for prev_idx in range(current_idx - 1, -1, -1):
        prev_number = nums[prev_idx]

        if current_number > prev_number and dp[1][prev_idx] + 1 >= dp[0][current_idx]:
            dp[0][current_idx] = dp[1][prev_idx] + 1
            parent[0][current_idx] = prev_idx

        if current_number < prev_number and dp[0][prev_idx] + 1 >= dp[1][current_idx]:
            dp[1][current_idx] = dp[0][prev_idx] + 1
            parent[1][current_idx] = prev_idx

    if dp[0][current_idx] > best_size:
        best_size = dp[0][current_idx]
        best_row = 0
        best_col = current_idx

    if dp[1][current_idx] > best_size:
        best_size = dp[1][current_idx]
        best_row = 1
        best_col = current_idx

result = deque()
while best_col is not None:
    result.appendleft(nums[best_col])
    best_col = parent[best_row][best_col]
    best_row = 1 if best_row == 0 else 0

print(*result, sep=' ')
