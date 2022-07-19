def dfs(node, graph, visited, cycles):
    # if cycle goes to Exception
    if node in cycles:
        raise Exception

    # if node is already in visited set
    if node in visited:
        return

    # add node in visited set
    visited.add(node)
    # add node in cycles set
    cycles.add(node)

    # walk through all children of current node
    for child in graph[node]:
        dfs(child, graph, visited, cycles)

    # remove node from current cycle
    cycles.remove(node)


graph = {}

# build graph from input
while True:
    line = input()
    if line == "End":
        break
    source, destination = line.split('-')
    # check current source is part of graph
    if source not in graph:
        graph[source] = []
    # check current destination is part of graph
    if destination not in graph:
        graph[destination] = []

    graph[source].append(destination)

visited = set()

try:
    # run dfs for all the nodes in graph
    for node in graph:
        dfs(node, graph, visited, set())
    print('Acyclic: Yes')
except Exception:
    print('Acyclic: No')
