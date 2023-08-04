# exam: 02. Topological Sorting
# judge: N/A

"""
Topological sorting using DFS with cycle detection
"""
from collections import deque


def dfs(node, graph, visited, cycles, sorted_nodes):
    if node in cycles:
        raise Exception('Cycle has been detected. Invalid topological sorting!')

    if node in visited:
        return

    visited.add(node)
    cycles.add(node)

    for child in graph[node]:
        dfs(child, graph, visited, cycles, sorted_nodes)

    cycles.remove(node)
    sorted_nodes.appendleft(node)


nodes = int(input())
graph = {}
for _ in range(nodes):
    line = input().split('->')
    node = line[0].strip()
    childs = line[1].strip().split(', ') if line[1] else []
    graph[node] = childs

visited = set()
cycles = set()
sorted_nodes = deque()

for node in graph:
    dfs(node, graph, visited, cycles, sorted_nodes)

print(f'Topological sorting: {", ".join(sorted_nodes)}')
