# exam: 02. Cycles in Graph
# https://judge.softuni.org/Contests/Compete/Index/3463#1

"""
Solution with DFS
"""


def dfs(node, graph, visited, path):
    if node in path:
        raise Exception

    if node in visited:
        return

    visited.add(node)
    path.add(node)

    for child in graph[node]:
        dfs(child, graph, visited, path)

    path.remove(node)


graph = {}

while True:
    line = input()

    if line == 'End':
        break

    source, destination = line.split('-')
    if source not in graph:
        graph[source] = []
    if destination not in graph:
        graph[destination] = []

    graph[source].append(destination)

visited = set()

try:
    for node in graph:
        dfs(node, graph, visited, set())

    print('Acyclic: Yes ')

except Exception:
    print('Acyclic: No')
