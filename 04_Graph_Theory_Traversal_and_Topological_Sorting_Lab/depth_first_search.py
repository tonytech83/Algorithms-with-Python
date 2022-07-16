def dfs(node, graph, visited):
    # if node is visited
    if node in visited:
        return

    # if node not visited, add it in visited set
    visited.add(node)

    # recursion - walk through all nodes
    for child in graph[node]:
        dfs(child, graph, visited)

    # print the last node
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
    6: []
}

visited = set()

for node in graph:
    dfs(node, graph, visited)
