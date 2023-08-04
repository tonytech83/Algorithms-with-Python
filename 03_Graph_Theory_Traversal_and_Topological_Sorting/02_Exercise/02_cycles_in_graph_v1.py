# exam: 02. Cycles in Graph
# https://judge.softuni.org/Contests/Compete/Index/3463#1

def find_dependencies(graph):
    result = {}

    for node, childs in graph.items():
        if node not in result:
            result[node] = 0

        for child in childs:
            if child not in result:
                result[child] = 1
            else:
                result[child] += 1

    return result


def find_node_without_dependencies(dependencies):
    for node, depend in dependencies.items():
        if depend == 0:
            return node

    return None


graph = {}

while True:
    line = input()

    if line == 'End':
        break

    node, child = line.split('-')

    if node not in graph:
        graph[node] = []
    graph[node].append(child)

dependencies = find_dependencies(graph)
has_cycle = False

while dependencies:
    node_to_remove = find_node_without_dependencies(dependencies)

    if not node_to_remove:
        has_cycle = True
        break

    if node_to_remove in graph:
        for child in graph[node_to_remove]:
            dependencies[child] -= 1

    dependencies.pop(node_to_remove)

if has_cycle:
    print('Acyclic: No')
else:
    print('Acyclic: Yes')
