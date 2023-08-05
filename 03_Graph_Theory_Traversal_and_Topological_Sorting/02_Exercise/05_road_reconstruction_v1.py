"""
exam: 05. Road Reconstruction
judge: https://judge.softuni.org/Contests/Compete/Index/3463#4

Solution with DFS and dictionary
"""


def dfs(node, destination, town, visited):
    if node in visited:
        return

    visited.add(node)

    if node == destination:
        return

    for child in town[node]:
        dfs(child, destination, town, visited)


def not_path(source, destination, town):
    visited = set()

    dfs(source, destination, town, visited)

    return destination not in visited


buildings_count = int(input())
streets_count = int(input())

town = {}
streets = []

for _ in range(streets_count):
    source, destination = input().split(' - ')
    streets.append((source, destination))
    streets.append((destination, source))

    if source not in town:
        town[source] = []
    town[source].append(destination)

    if destination not in town:
        town[destination] = []
    town[destination].append(source)

important_streets = []

for source, destination in sorted(streets, key=lambda t: (t[0], t[1])):
    if source not in town[destination] or destination not in town[source]:
        continue

    town[source].remove(destination)
    town[destination].remove(source)

    if not_path(source, destination, town):
        important_streets.append((source, destination))
    else:
        town[source].append(destination)
        town[destination].append(source)

print('Important streets:')
[print(f'{source} {destination}') for source, destination in important_streets]
