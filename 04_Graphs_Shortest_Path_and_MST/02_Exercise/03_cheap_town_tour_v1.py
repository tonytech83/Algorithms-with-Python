"""
exam: 03. Cheap Town Tour
judge: https://judge.softuni.org/Contests/Practice/Index/3465#2

Solved with Kruskal algorithm
"""


def find_root(parent, node):
    while node != parent[node]:
        node = parent[node]

    return node


towns_count = int(input())
roads_count = int(input())

graph = []

for _ in range(roads_count):
    first, second, weight = [int(x) for x in input().split(' - ')]
    graph.append((first, second, weight))

parent = [n for n in range(towns_count)]
total_cost = 0

for first, second, weight in sorted(graph, key=lambda e: e[2]):
    first_node_root = find_root(parent, first)
    second_node_root = find_root(parent, second)

    if first_node_root != second_node_root:
        parent[first_node_root] = second_node_root
        total_cost += weight

print(f'Total cost: {total_cost}')
