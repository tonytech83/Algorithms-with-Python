# exam: 04. Break Cycles
# judge: https://judge.softuni.org/Contests/Compete/Index/3463#3

"""
Solution with DFS
"""


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
    node, childs = input().split(' -> ')
    graph[node] = [x for x in childs.split()]
    for child in childs.split():
        edges.append((node, child))

removed_edges = []

for source, destination in sorted(edges, key=lambda t: (t[0], t[1])):
    if destination not in graph[source] or source not in graph[destination]:
        continue

    # removes edges between source and destination
    graph[source].remove(destination)
    graph[destination].remove(source)

    if path_exists(source, destination, graph):
        removed_edges.append((source, destination))
    else:
        # if path not exist returns the edges
        graph[source].append(destination)
        graph[destination].append(source)

print(f'Edges to remove: {len(removed_edges)}')
[print(f'{source} - {destination}') for source, destination in removed_edges]
