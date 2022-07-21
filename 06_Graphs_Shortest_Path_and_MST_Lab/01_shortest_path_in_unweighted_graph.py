# using BFS

from collections import deque

nodes = int(input())
edges = int(input())

graph = []
[graph.append([]) for _ in range(nodes + 1)]

for _ in range(edges):
    source, destination = [int(x) for x in input().split()]
    graph[source].append(destination)

start_node = int(input())
destination_node = int(input())

visited = [False] * (nodes + 1)
# contains parent node for each child node
parent = [None] * (nodes + 1)

# mark start_note as visited
visited[start_node] = True

# create queue
queue = deque([start_node])

while queue:
    node = queue.popleft()
    if node == destination_node:
        break
    for child in graph[node]:
        if visited[child]:
            continue
        # if not visited, mark it as visited
        visited[child] = True
        # add it in queue
        queue.append(child)
        # mark current node as parent to current child
        parent[child] = node

path = deque()
node = destination_node

while node is not None:
    path.appendleft(node)
    node = parent[node]

print(f"Shortest path length is: {len(path) - 1}")
print(*path, sep=' ')
