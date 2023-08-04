# exam: 01. Areas in Matrix
# judge: https://judge.softuni.org/Contests/Compete/Index/3463#0

def dfs(row, col, matrix, visited, parent):
    if row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix[0]):
        return

    if visited[row][col]:
        return

    if matrix[row][col] != parent:
        return

    visited[row][col] = True

    dfs(row + 1, col, matrix, visited, parent)
    dfs(row - 1, col, matrix, visited, parent)
    dfs(row, col + 1, matrix, visited, parent)
    dfs(row, col - 1, matrix, visited, parent)


rows = int(input())
cols = int(input())

matrix = [list(input()) for _ in range(rows)]
visited = [[False] * cols for _ in range(rows)]
areas = {}
total_areas = 0

for row in range(rows):
    for col in range(cols):
        if visited[row][col]:
            continue

        key = matrix[row][col]

        dfs(row, col, matrix, visited, key)

        if key not in areas:
            areas[key] = 0

        areas[key] += 1
        total_areas += 1

print(f'Areas: {total_areas}')
[print(f"Letter '{area}' -> {count}") for area, count in sorted(areas.items())]
