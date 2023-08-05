"""
Depth First Search (DFS) algorithm example
Used Array to store graph (when have consecutive numbers for node names)
"""


def dfs(node, graph, visited):
    # BASE CASE if node is visited (the value is True)
    if visited[node]:
        return

    # Mark the node as visited (True)
    visited[node] = True

    # Recursion - walk through all childs of the node
    for child in graph[node]:
        dfs(child, graph, visited)

    # print the last node which hasn't childs
    print(node, end=' ')


graph = [
    [3, 6],
    [2, 3, 4, 5, 6],
    [1, 4, 5],
    [0, 1, 5],
    [1, 2, 6],
    [1, 2, 3],
    [0, 1, 4]
]

# mark all nodes as not visited (False)
visited = [False] * len(graph)

for node in range(len(graph)):
    dfs(node, graph, visited)
