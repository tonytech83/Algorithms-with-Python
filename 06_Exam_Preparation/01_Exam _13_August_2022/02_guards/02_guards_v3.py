"""
exam: 02. Guards
judge: https://judge.softuni.org/Contests/Practice/Index/3592#1

Solution with DFS and list as graph
"""


def dfs(node, graph, unvisited_nodes):
    if node not in unvisited_nodes:
        return

    unvisited_nodes.remove(node)

    for child in graph[node]:
        dfs(child, graph, unvisited_nodes)


nodes = int(input())
edges = int(input())

graph = [[] for x in range(nodes + 1)]

for _ in range(edges):
    source, destination = [int(x) for x in input().split()]
    graph[source].append(destination)

start_node = int(input())

unvisited_nodes = list(x for x in range(1, nodes + 1))

dfs(start_node, graph, unvisited_nodes)

print(*unvisited_nodes, sep=' ')
