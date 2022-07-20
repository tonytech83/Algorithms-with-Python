def dfs(building, graph, visited):
    if visited[building]:
        return

    visited[building] = True

    for child in graph[building]:
        dfs(child, graph, visited)


buildings = int(input())
streets = int(input())

graph = []
[graph.append([]) for _ in range(buildings)]

edges = []

for _ in range(streets):
    first, second = [int(x) for x in input().split(' - ')]
    graph[first].append(second)
    graph[second].append(first)
    edges.append((min(first, second), max(first, second)))

important_streets = []

for first, second in edges:
    graph[first].remove(second)
    graph[second].remove(first)

    visited = [False] * buildings

    dfs(0, graph, visited)

    if not all(visited):
        important_streets.append((first, second))

    graph[first].append(second)
    graph[second].append(first)

print("Important streets:")
for first, second in important_streets:
    print(f"{first} {second}")
