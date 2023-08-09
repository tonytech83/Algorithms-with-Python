"""
exam: 03. Chain Lightning
judge: https://judge.softuni.org/Contests/Practice/Index/3474#2

# MTS -> Prim's Algorithm
"""
from queue import PriorityQueue


class Edge:
    def __init__(self, first, second, distance):
        self.first = first
        self.second = second
        self.distance = distance

    def __gt__(self, other):
        return self.distance > other.distance


def calc_damage(jumps_count, damage):
    for _ in range(jumps_count):
        damage //= 2

    return damage


def prim(node, graph, damage, damage_per_node):
    damage_per_node[node] += damage

    tree = {node}
    jumps = [0] * len(graph)

    pq = PriorityQueue()
    [pq.put(edge) for edge in graph[node]]

    while not pq.empty():
        min_edge = pq.get()
        tree_node, non_tree_node = -1, None

        if min_edge.first in tree and min_edge.second not in tree:
            tree_node, non_tree_node = min_edge.first, min_edge.second

        if min_edge.first not in tree and min_edge.second in tree:
            tree_node, non_tree_node = min_edge.second, min_edge.first

        if non_tree_node is None:
            continue

        tree.add(non_tree_node)
        [pq.put(edge) for edge in graph[non_tree_node]]

        jumps[non_tree_node] = jumps[tree_node] + 1
        damage_per_node[non_tree_node] += calc_damage(jumps[non_tree_node], damage)


nodes = int(input())
edges = int(input())
lightning_count = int(input())

graph = {node: [] for node in range(nodes)}

for _ in range(edges):
    first, second, distance = [int(x) for x in input().split()]

    edge = Edge(first, second, distance)
    graph[first].append(edge)
    graph[second].append(edge)

damage_per_node = [0] * nodes

for _ in range(lightning_count):
    node, damage = [int(x) for x in input().split()]
    prim(node, graph, damage, damage_per_node)

print(max(damage_per_node))
