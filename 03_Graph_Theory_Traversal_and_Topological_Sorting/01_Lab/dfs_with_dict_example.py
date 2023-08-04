"""
Depth First Search (DFS) algorithm example
Used Dictionary to store graph (when have strings or non-consecutive numbers for node names)
"""


def dfs(node, graph, visited):
    # BASE CASE if node is visited
    if node in visited:
        return

    # Add node to visited set
    visited.add(node)

    # Recursion - walk through all childs of the node
    for child in graph[node]:
        dfs(child, graph, visited)

    # print the last node which hasn't childs
    print(node, end=' ')


graph = {
    1: [19, 21, 14],
    19: [7, 12, 31, 21],
    7: [1],
    12: [],
    31: [21],
    21: [14],
    14: [23, 6],
    23: [21],
    6: [],
}

visited = set()

for node in graph:
    dfs(node, graph, visited)
