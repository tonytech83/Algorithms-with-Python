def dfs(node, graph, visited):
    # if node is visited
    if visited[node]:
        return

    # if node is not visited, marked it as visited = True
    visited[node] = True

    # for any node try visit all child in his array
    for child in graph[node]:
        dfs(child, graph, visited)

    print(node, end=' ')


graph = [
    [3, 6],
    [3, 6, 4, 2, 5],
    [1, 4, 5],
    [5, 0, 1],
    [1, 2, 6],
    [2, 1, 3],
    [0, 1, 4]
]

# mark all nodes as not visited = False
visited = [False] * len(graph)

for node in range(len(graph)):
    dfs(node, graph, visited)
