# MST using Kruskal's algorithm
def find_root(parent, node):
    while node != parent[node]:
        node = parent[node]
    return node


nodes = int(input())
edges = int(input())

graph = []

# create graph from input
for _ in range(edges):
    first, second, weight = [int(x) for x in input().split(' - ')]
    graph.append((first, second, weight))

# create array with all nodes as parents (Kruskal's algorithm)
parent = [num for num in range(nodes)]

# calc the weight of our MST
total_cost = 0

for first, second, weight in sorted(graph, key=lambda x: x[2]):
    first_node_root = find_root(parent, first)
    second_node_root = find_root(parent, second)

    if first_node_root == second_node_root:
        continue

    # merge the two nodes(trees) into one tree
    parent[first_node_root] = second_node_root

    total_cost += weight

print(f'Total cost: {total_cost}')
