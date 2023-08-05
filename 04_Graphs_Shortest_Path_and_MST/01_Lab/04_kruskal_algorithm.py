"""
exam: 04. Kruskal's Algorithm
judge: https://judge.softuni.org/Contests/Compete/Index/3464#3

Minimum Spanning Tree (MST) with Kruskal's algorithm
 - Create a forest F holding all graph vertices and no edges
 - Create a set S holding all edges in the graph
 - While S is non-empty
    - Remove the edge e with min weight
    - If e connects two different trees
        - Add e to the forest
        - Join these two trees into a single tree
- The graph may not be connected
"""


class Edge:
    def __init__(self, first, second, weight):
        self.first = first
        self.second = second
        self.weight = weight


def find_root(parent, node):
    while node != parent[node]:
        node = parent[node]

    # return root when node is root for him self
    return node


edges = int(input())
graph = []

# used it to found max node, to determinate size of parent array
max_node = float('-inf')

for _ in range(edges):
    first, second, weight = [int(x) for x in input().split(', ')]
    graph.append(Edge(first, second, weight))
    max_node = max(first, second, max_node)

# create parent array where initially all nodes has themselves as root
# node (idx)    0 1 2 3 4 ... max_node
# parent        0 1 2 3 4 ... max_node
parent = [n for n in range(max_node + 1)]

# create array to store edges
forest = []

for edge in sorted(graph, key=lambda e: e.weight):
    first_node_root = find_root(parent, edge.first)
    second_node_root = find_root(parent, edge.second)

    # if True, attaches first_root to second_root
    if first_node_root != second_node_root:
        parent[first_node_root] = second_node_root
        forest.append(edge)

[print(f'{edge.first} - {edge.second}') for edge in forest]
