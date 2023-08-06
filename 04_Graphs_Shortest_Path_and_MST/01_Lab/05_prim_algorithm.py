"""
exam: 05. Prim's Algorithm
judge: https://judge.softuni.org/Contests/Compete/Index/3464#3

Minimum Spanning Tree (MST) with Prim's algorithm using PriorityQueue
- Given a graph G(V, E) find the minimum spanning forest T(V', E')
- Attach to the tree T the starting node
- While smallest edge exists
    - Attach to T the smallest possible edge from G without creating a cycle in T
        - Use the smallest edge (u, v),such that u ∈ T and v ∉ T
- Start the Prim's algorithm for each node from G
"""
from queue import PriorityQueue


class Edge:
    def __init__(self, first, second, weight):
        self.first = first
        self.second = second
        self.weight = weight

    def __gt__(self, other):
        return self.weight > other.weight


def prim(node, graph, forest, forest_edges):
    # add node to forest array
    forest.add(node)

    pq = PriorityQueue()

    for current_edge in graph[node]:
        pq.put(current_edge)

    while not pq.empty():
        min_edge = pq.get()
        non_tree_node = None

        if min_edge.first in forest and min_edge.second not in forest:
            non_tree_node = min_edge.second

        if min_edge.first not in forest and min_edge.secong in forest:
            non_tree_node = min_edge.first

        if non_tree_node is None:
            continue

        forest.add(non_tree_node)
        forest_edges.append(min_edge)

        for edge in graph[non_tree_node]:
            pq.put(edge)


edges = int(input())

graph = {}

for _ in range(edges):
    first, second, weight = [int(x) for x in input().split(', ')]

    if first not in graph:
        graph[first] = []

    if second not in graph:
        graph[second] = []

    edge = Edge(first, second, weight)
    graph[first].append(edge)
    graph[second].append(edge)

forest = set()
forest_edges = []

for node in graph:
    if node in forest:
        continue

    prim(node, graph, forest, forest_edges)

[print(f'{edge.first} - {edge.second}') for edge in forest_edges]
