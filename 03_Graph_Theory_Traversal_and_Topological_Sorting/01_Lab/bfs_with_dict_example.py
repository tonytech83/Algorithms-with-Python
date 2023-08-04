"""
Breadth-First Search (BFS) algorithm example
Used Dictionary to store graph
"""
from collections import deque


def bfs(node, graph, visited, queue):
    if visited[node]:
        return

    # add node to queue and mark it as visited (True)
    queue.append(node)
    visited[node] = True

    while queue:
        current_node = queue.popleft()
        print(current_node, end=' ')

        for child in graph[node]:
            if not visited[node]:
                queue.add(child)
                visited[child] = True


graph = {
    7: [19, 21, 14],
    19: [1, 12, 31, 21],
    21: [14],
    14: [23, 6],
    1: [7],
    12: [],
    31: [21],
    23: [21],
    6: [],
}

# dict to mark visited nodes
visited = {x: False for x in graph}
queue = deque()

for node in graph:
    bfs(node, graph, visited, queue)
