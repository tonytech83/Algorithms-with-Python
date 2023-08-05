"""
exam: 01. Shortest Path in Unweighted Graph
judge: https://judge.softuni.org/Contests/Compete/Index/3464#0

Finding the shortest path in unweighted graph using BFS
"""
from collections import deque


def find_parent_by_node(start, end, graph):
    visited = [False] * len(graph)

    # contains parent node for each child node
    parent = [None] * len(graph)

    # mark start as visited and adds to queue
    visited[start] = True
    queue = deque([start])

    while queue:
        node = queue.popleft()

        if node == end:
            break

        for child in graph[node]:
            if visited[child]:
                continue

            # if not visited, mark it as visited
            visited[child] = True

            # add it in queue
            queue.append(child)

            # mark current node as parent to current child
            parent[child] = node

    return parent


def reconstruct_path(parent, end):
    path = deque()
    node = end

    while node is not None:
        path.appendleft(node)
        node = parent[node]

    return path


nodes = int(input())
edges = int(input())

graph = []
[graph.append([]) for _ in range(nodes + 1)]

for _ in range(edges):
    source, destination = [int(x) for x in input().split()]
    graph[source].append(destination)

start = int(input())
end = int(input())

parent = find_parent_by_node(start, end, graph)
path = reconstruct_path(parent, end)

print(f"Shortest path length is: {len(path) - 1}")
print(*path, sep=' ')
