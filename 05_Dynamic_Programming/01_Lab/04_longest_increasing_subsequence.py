"""
exam: 04. Longest Increasing Subsequence
judge: https://judge.softuni.org/Contests/Practice/Index/3471#3

Find the largest subsequence of increasing numbers within a given sequence
- The subsequence is not necessary to be contiguous or unique
"""
from collections import deque

nums = [int(x) for x in input().split()]

# store best len for each cell
size = [0] * len(nums)
# base case -> only one element in sequence has 1 as size
size[0] = 1
# store the parent for current cell (longest)
parent = [None] * len(nums)

for current in range(1, len(nums)):
    current_number = nums[current]
    current_best_size = 1
    current_parent = None

    for prev in range(current - 1, -1, - 1):
        prev_number = nums[prev]

        if prev_number >= current_number:
            continue

        if size[prev] + 1 >= current_best_size:
            current_best_size = size[prev] + 1
            current_parent = prev

    size[current] = current_best_size
    parent[current] = current_parent

# Longest Increasing Subsequence size
# print(max(size))

best_idx = size.index(max(size))

# reconstruct elements of LIS
result = deque()
while best_idx is not None:
    result.appendleft(nums[best_idx])
    best_idx = parent[best_idx]

print(*result, sep=' ')
