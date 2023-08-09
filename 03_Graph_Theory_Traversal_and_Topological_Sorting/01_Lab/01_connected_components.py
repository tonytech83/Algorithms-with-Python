# exam: 01. Connected Components
# judge: https://judge.softuni.org/Contests/Compete/Index/3462#0

def dfs(node, graph, visited, components):
    if node in visited:
        return

    visited.add(node)

    for child in graph[node]:
        dfs(child, graph, visited, components)

    components.append(node)


nodes = int(input())

graph = {}
for node in range(nodes):
    line = input()
    childs = [] if line == '' else [int(x) for x in line.split()]
    graph[node] = childs

visited = set()
for node in graph:
    if node in visited:
        continue

    components = []
    dfs(node, graph, visited, components)
    print(f"Connected component: {' '.join([str(x) for x in components])}")
