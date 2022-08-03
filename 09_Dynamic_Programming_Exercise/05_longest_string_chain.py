# Longest increasing subsequence

from collections import deque

strings = input().split()

size = [0] * len(strings)
prev = [None] * len(strings)

best_size = 0
best_idx = 0

for idx in range(len(strings)):
    current_string = strings[idx]
    current_size = 1
    parent = None

    for prev_idx in range(idx - 1, -1, -1):
        prev_string = strings[prev_idx]

        if len(prev_string) >= len(current_string):
            continue

        if size[prev_idx] + 1 >= current_size:
            current_size = size[prev_idx] + 1
            parent = prev_idx

    size[idx] = current_size
    prev[idx] = parent

    if current_size > best_size:
        best_size = current_size
        best_idx = idx

# Longest increasing subsequence
lis = deque()

idx = best_idx
while idx is not None:
    lis.appendleft(strings[idx])
    idx = prev[idx]

print(*lis, sep=' ')
