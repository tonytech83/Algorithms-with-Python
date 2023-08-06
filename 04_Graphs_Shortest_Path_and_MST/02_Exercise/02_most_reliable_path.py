"""
exam: 02. Most Reliable Path
judge: https://judge.softuni.org/Contests/Practice/Index/3465#1

Modified Dijkstra to find path with the biggest distance with array
"""
from collections import deque
from queue import PriorityQueue


class Edge:
    def __init__(self, first, second, weight):
        self.first = first
        self.second = second
        self.weight = weight


nodes = int(input())
edges = int(input())

graph = []
[graph.append([]) for _ in range(nodes)]

for _ in range(edges):
    first, second, weight = [int(x) for x in input().split()]
    edge = Edge(first, second, weight)
    graph[first].append(edge)
    graph[second].append(edge)

start_node = int(input())
target_node = int(input())

distance = [float('-inf')] * nodes
distance[start_node] = 100

parent = [None] * nodes

pq = PriorityQueue()
pq.put((-100, start_node))

while not pq.empty():
    max_distance, node = pq.get()

    if node == target_node:
        break

    for edge in graph[node]:
        child = edge.second if edge.first == node else edge.first
        new_distance = -max_distance * edge.weight / 100
        if new_distance > distance[child]:
            distance[child] = new_distance
            parent[child] = node
            pq.put((-new_distance, child))

print(f'Most reliable path reliability: {distance[target_node]:.2f}%')

path = deque()
node = target_node
while node is not None:
    path.appendleft(node)
    node = parent[node]

print(*path, sep=' -> ')
