from collections import deque

trading_pairs = int(input())

graph = {}

for _ in range(trading_pairs):
    source, destination, price = [str(x) for x in input().split(' ')]
    if source not in graph:
        graph[source] = []
        graph[source].append((destination, float(price)))
    else:
        graph[source].append((destination, float(price)))

currency = input()

path = [f'{currency}: 1.000']
path_currency = [currency]
current_value = 1

queue = deque()
queue.append(currency)
visited = set()

while queue:
    current_currency = queue.popleft()
    visited.add(current_currency)

    next_currency, price = max(graph[current_currency], key=lambda i: i[1])
    current_value = current_value * price
    path.append(f'{next_currency}: {current_value:.3f}')
    path_currency.append(next_currency)

    if next_currency not in visited:
        queue.append(next_currency)

if current_value < 1:
    print("False")
    path.pop()
    print(*path, sep='\n')
elif current_value > 1:
    print("True")
    print(*path_currency, sep=' ')
