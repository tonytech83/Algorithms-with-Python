from collections import deque


def find_shortest_path(graph, source, destination):
    queue = deque([source])
    visited = {source}
    parent = {source: None}

    while queue:
        node = queue.popleft()
        if node == destination:
            break
        for child in graph[node]:
            if child in visited:
                continue
            queue.append(child)
            visited.add(child)
            parent[child] = node

    return parent


def find_path_size(parent, destination):
    node = destination
    size = 0

    while node is not None:
        node = parent[node]
        size += 1

    return size - 1


nodes = int(input())
pairs = int(input())

graph = {}

# read graph
for _ in range(nodes):
    node_str, children_str = input().split(':')
    node = int(node_str)
    # split children from string and convert to int
    children = [int(x) for x in children_str.split()] if children_str else []
    graph[node] = children

# read pairs
for _ in range(pairs):
    source, destination = [int(x) for x in input().split('-')]

    # search with BFS
    parent = find_shortest_path(graph, source, destination)

    # no path from source to destination
    if destination not in parent:
        print(f'{{{source}, {destination}}} -> -1')
        continue

    size = find_path_size(parent, destination)

    print(f'{{{source}, {destination}}} -> {size}')
