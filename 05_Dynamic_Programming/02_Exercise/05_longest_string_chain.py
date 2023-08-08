"""
exam: 05. Longest String Chain
judge: https://judge.softuni.org/Contests/Compete/Index/3473#4

solution with LIS
"""
from collections import deque


# Exam:
# input: a   ab  abcd   abc  abcd    abcde
# size:  1   2   3      3     4       5
# prev: -1   0   1      1     3       4

def lis(size, prev):
    for idx in range(1, len(list_str)):
        current_str = list_str[idx]
        current_best_size = 1
        current_parent = None

        for prev_idx in range(idx - 1, -1, -1):
            prev_str = list_str[prev_idx]

            if len(prev_str) >= len(current_str):
                continue

            new_best_size = size[prev_idx] + 1

            if new_best_size >= current_best_size:
                current_best_size = new_best_size
                current_parent = prev_idx

        size[idx] = current_best_size
        prev[idx] = current_parent


def reconstruct_lis(best_idx, list_str, prev):
    result = deque()

    while best_idx is not None:
        result.appendleft(list_str[best_idx])
        best_idx = prev[best_idx]

    return result


list_str = [x for x in input().split()]

size = [0] * len(list_str)
size[0] = 1

prev = [None] * len(list_str)

lis(size, prev)

best_idx = size.index(max(size))

print(*reconstruct_lis(best_idx, list_str, prev), sep=' ')
