from collections import deque

closing_prices = [int(x) for x in input().split(', ')]
max_change = int(input())

size = [0] * len(closing_prices)
size[0] = 1
parents = [None] * len(closing_prices)

for idx in range(1, len(closing_prices)):
    current_price = closing_prices[idx]
    current_best = 1
    parent = None

    for prev in range(idx - 1, -1, -1):
        prev_price = closing_prices[prev]

        if current_price <= prev_price or (current_price - prev_price) > max_change:
            continue

        if size[prev] + 1 >= current_best:
            current_best = size[prev] + 1
            parent = prev

    size[idx] = current_best
    parents[idx] = parent

best_idx = size.index(max(size))

result = deque()
while best_idx is not None:
    result.appendleft(closing_prices[best_idx])
    best_idx = parents[best_idx]

print(*result, sep=' ')
