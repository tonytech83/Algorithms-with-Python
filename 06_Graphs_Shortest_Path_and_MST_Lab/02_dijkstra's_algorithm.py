# using BFS

import sys
from queue import PriorityQueue
from collections import deque


class Edge:
    def __init__(self, source, destination, weight):
        self.source = source
        self.destination = destination
        self.weight = weight


edges = int(input())

# graph dictionary
graph = {}

for _ in range(edges):
    source, destination, weight = [int(x) for x in input().split(', ')]
    # if source is not part of graph, add with empty array
    if source not in graph:
        graph[source] = []
    # if destination is not part of graph, add with empty array
    if destination not in graph:
        graph[destination] = []
    # add for every source all edges
    graph[source].append(Edge(source, destination, weight))

start = int(input())
end = int(input())

# search for max node to determinate the length of distance array
max_node = max(graph.keys())

# create distance array (sys.maxsize can be replaced with float('inf')
distance = [sys.maxsize] * (max_node + 1)
# create parent array
parent = [None] * (max_node + 1)

distance[start] = 0

pq = PriorityQueue()
# first is weight, because PriorityQueue always sort by first element
pq.put((0, start))

while not pq.empty():
    min_distance, node = pq.get()
    if node == end:
        break
    for edge in graph[node]:
        new_distance = min_distance + edge.weight
        if new_distance < distance[edge.destination]:
            distance[edge.destination] = new_distance
            parent[edge.destination] = node
            pq.put((new_distance, edge.destination))

if distance[end] == sys.maxsize:
    print('There is no such path.')
else:
    print(distance[end])

    path = deque()
    node = end
    while node is not None:
        path.appendleft(node)
        node = parent[node]
    print(*path, sep=' ')
