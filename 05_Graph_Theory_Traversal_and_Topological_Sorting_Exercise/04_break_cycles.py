def dfs(node, destination, graph, visited):
    if node in visited:
        return

    visited.add(node)

    if node == destination:
        return

    for child in graph[node]:
        dfs(child, destination, graph, visited)


def path_exists(source, destination, graph):
    visited = set()

    dfs(source, destination, graph, visited)

    return destination in visited


nodes = int(input())

graph = {}

# create array where to store all edges
# for example if we have: 1 -> 2 5 4
# we will store in edges array (1, 2), (1, 5), (1, 4)
edges = []

for _ in range(nodes):
    node, children_str = input().split(" -> ")
    children = children_str.split()
    graph[node] = children
    for child in children:
        edges.append((node, child))

# keep removed edges
removed_edges = []

for source, destination in sorted(edges, key=lambda x: (x[0], x[1])):
    if destination not in graph[source] or source not in graph[destination]:
        continue
    graph[source].remove(destination)
    graph[destination].remove(source)

    if path_exists(source, destination, graph):
        removed_edges.append((source, destination))

    else:
        graph[source].append(destination)
        graph[destination].append(source)

print(f'Edges to remove: {len(removed_edges)}')
for first, second in removed_edges:
    print(f"{first} - {second}")
