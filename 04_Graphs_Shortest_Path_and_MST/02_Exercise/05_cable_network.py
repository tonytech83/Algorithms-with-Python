"""
exam: 05. Cable Network
judge: https://judge.softuni.org/Contests/Practice/Index/3465#4

Solution with Prim's algorithm
"""
from queue import PriorityQueue


class Edge:
    def __init__(self, first, second, weight):
        self.first = first
        self.second = second
        self.weight = weight

    def __gt__(self, other):
        return self.weight > other.weight


budget = int(input())
nodes = int(input())
edges = int(input())

forest = set()
graph = []
[graph.append([]) for _ in range(nodes)]

for _ in range(edges):
    line = input().split()
    first, second, weight = int(line[0]), int(line[1]), int(line[2])
    edge = Edge(first, second, int(weight))
    graph[first].append(edge)
    graph[second].append(edge)

    if 'connected' in line:
        forest.add(first)
        forest.add(second)

pq = PriorityQueue()
# add all edges which are connected already
for node in forest:
    for edge in graph[node]:
        pq.put(edge)

budget_used = 0

while not pq.empty():
    min_edge = pq.get()
    non_tree_node = None

    if min_edge.first in forest and min_edge.second not in forest:
        non_tree_node = min_edge.second

    if min_edge.first not in forest and min_edge.second in forest:
        non_tree_node = min_edge.first

    if non_tree_node is None:
        continue

    if budget_used + min_edge.weight > budget:
        break

    budget_used += min_edge.weight

    forest.add(non_tree_node)

    for edge in graph[non_tree_node]:
        pq.put(edge)

print(f'Budget used: {budget_used}')
