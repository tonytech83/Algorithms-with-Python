"""
exam: 02. Guards
judge: https://judge.softuni.org/Contests/Practice/Index/3592#1
"""
from collections import deque

nodes = int(input())
edges = int(input())

graph = [[] for _ in range(nodes + 1)]

for _ in range(edges):
    source, destination = [int(x) for x in input().split()]
    graph[source].append(destination)

start_node = int(input())

visited = [False] * (nodes + 1)
visited[start_node] = True
visited[0] = True

parent = [None] * (nodes + 1)
parent[0] = 0
parent[start_node] = start_node

queue = deque()
queue.append(start_node)

while queue:
    node = queue.popleft()

    for child in graph[node]:
        if visited[child]:
            continue

        visited[child] = True
        queue.append(child)
        parent[child] = node

path = deque()

for idx, node in enumerate(parent):
    if node is None:
        path.append(idx)
    else:
        continue

print(*path, sep=' ')
