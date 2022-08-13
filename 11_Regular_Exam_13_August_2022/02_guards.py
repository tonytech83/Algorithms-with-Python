from collections import deque

nodes = int(input())
edges = int(input())

graph = []
[graph.append([]) for _ in range(nodes + 1)]

for _ in range(edges):
    source, destination = [int(x) for x in input().split(' ')]
    graph[source].append(destination)

start_node = int(input())

visited = [False] * (nodes + 1)

parent = [None] * (nodes + 1)
parent[0] = 0
parent[start_node] = start_node

visited[start_node] = True

# create queue
queue = deque([start_node])

while queue:
    node = queue.popleft()
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

for index, node in enumerate(parent):
    if node == None:
        path.append(index)
    else:
        continue
#
#
print(*path, sep=' ')
