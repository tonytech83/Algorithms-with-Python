"""
exam: 03. Arbitrage
judge: https://judge.softuni.org/Contests/Practice/Index/3592#2

Breadth-First Search (BFS) algorithm
"""
from collections import deque

trading_pairs = int(input())

graph = {}
# {'GBP': [('USD', 1.27)], 'USD': [('AUD', 1.43), ('NZD', 1.51)], 'NZD': [('AUD', 0.95)], 'AUD': [('GBP', 0.55)]}

for _ in range(trading_pairs):
    from_currency, to_currency, price = input().split()
    price = float(price)

    if from_currency not in graph:
        graph[from_currency] = []

    graph[from_currency].append((to_currency, price))

start_currency = input()
path = [f'{start_currency}: 1.000']
path_currency = [start_currency]
current_value = 1

queue = deque()
queue.append(start_currency)
visited = set()

while queue:
    current_currency = queue.popleft()
    visited.add(current_currency)

    next_currency, price = max(graph[current_currency], key=lambda p: p[1])
    current_value = current_value * price
    path.append(f'{next_currency}: {current_value:.3f}')
    path_currency.append(next_currency)

    if next_currency not in visited:
        queue.append(next_currency)

if current_value > 1:
    print('True')
    print(*path_currency, sep=' ')
else:
    print('False')
    path.pop()
    print('\n'.join(path))
