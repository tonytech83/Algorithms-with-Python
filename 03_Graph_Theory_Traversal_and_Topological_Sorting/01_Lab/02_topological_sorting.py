# exam: 02. Topological Sorting
# judge: https://judge.softuni.org/Contests/Compete/Index/3462#1

"""
Topological sorting (ordering) of directed graph
- Linear ordering of its nodes, such that:
    - For every directed edge from node A to node B, A comes before B in the ordering
- Rules:
    - Can not be used on undirected graphs
    - Graph with cycle cannot be sorted
    - Various sorting algorithms exists, and they give different results
"""


# Source Removal top-sorting algorithm
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


nodes = int(input())
graph = {}
for _ in range(nodes):
    line = input().split('->')
    node = line[0].strip()
    childs = line[1].strip().split(', ') if line[1] else []
    graph[node] = childs

sorted_elements = []

dependencies = find_dependencies(graph)
has_cycle = False

while dependencies:
    # takes element without dependencies
    node_to_remove = find_node_without_dependencies(dependencies)
    # break while because there is a cycle
    if not node_to_remove:
        has_cycle = True
        break

    # remove dependencies from child
    for child in graph[node_to_remove]:
        dependencies[child] -= 1

    # add element to sorted elements and remove the element from dependencies dict
    sorted_elements.append(node_to_remove)
    del dependencies[node_to_remove]

if has_cycle:
    print('Invalid topological sorting')
else:
    print(f'Topological sorting: {", ".join(sorted_elements)}')
