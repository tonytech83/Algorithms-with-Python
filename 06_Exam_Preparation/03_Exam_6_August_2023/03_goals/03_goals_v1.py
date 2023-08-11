"""
exam: 03. Goals
judge: https://judge.softuni.org/Contests/Practice/Index/4044#2

Using LIS (Find the largest subsequence of increasing numbers within a given sequence)
"""
from collections import deque

scored_goals = [int(x) for x in input().split(', ')]

size = [min(scored_goals)] * len(scored_goals)
size[0] = 1

parent = [None] * len(scored_goals)

for current in range(1, len(scored_goals)):
    current_result = scored_goals[current]
    current_best_size = 1
    current_parent = None

    for prev in range(current - 1, -1, -1):
        prev_result = scored_goals[prev]

        if prev_result > current_result:
            continue

        if size[prev] + 1 >= current_best_size:
            current_best_size = size[prev] + 1
            current_parent = prev

    size[current] = current_best_size
    parent[current] = current_parent

best_idx = size.index(max(size))
result = deque()
while best_idx is not None:
    result.appendleft(scored_goals[best_idx])
    best_idx = parent[best_idx]

print(*result, sep=' ')
