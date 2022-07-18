def dfs(parent, row, col, matrix, visited):
    # check is valid index - should be first
    if row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0]):
        return

    # base case #1 - check the current cell [row][col] is marked as visited (True) in visited matrix
    if visited[row][col]:
        return

    # base case #2 - check the current cell [row][col] match the parent
    if matrix[row][col] != parent:
        return

    # if all conditions above are False, mark the cell as visited -> True
    visited[row][col] = True

    dfs(parent, row - 1, col, matrix, visited)  # upper cell
    dfs(parent, row + 1, col, matrix, visited)  # lower cell
    dfs(parent, row, col - 1, matrix, visited)  # left cell
    dfs(parent, row, col + 1, matrix, visited)  # right cell


rows = int(input())
cols = int(input())

matrix = []
visited = []

for _ in range(rows):
    matrix.append(list(input()))
    # fill the new visited matrix with "False"
    visited.append([False] * cols)

areas = {}
total_areas = 0

for row in range(rows):
    for col in range(cols):
        if visited[row][col]:
            continue
        key = matrix[row][col]
        dfs(key, row, col, matrix, visited)
        # first time found this key
        if key not in areas:
            areas[key] = 1
        # if found more times
        else:
            areas[key] += 1
        total_areas += 1

print(f"Areas: {total_areas}")
for area, size in sorted(areas.items()):
    print(f"Letter '{area}' -> {size}")
