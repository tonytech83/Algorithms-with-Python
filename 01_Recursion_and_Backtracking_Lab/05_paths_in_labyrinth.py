def all_paths(row, col, matrix, direction, path):
    # pre-action
    # check index is outside of matrix
    if row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0]):
        return

    # check if index is *
    if matrix[row][col] == "*":
        return

    # mark index as visited
    if matrix[row][col] == "visited":
        return

    path.append(direction)

    # check if index is end point
    if matrix[row][col] == "e":
        print("".join(path))
    else:
        matrix[row][col] = "visited"
        # recursion
        all_paths(row, col - 1, matrix, "L", path)
        all_paths(row, col + 1, matrix, "R", path)
        all_paths(row - 1, col, matrix, "U", path)
        all_paths(row + 1, col, matrix, "D", path)
        matrix[row][col] = "-"

    # post-action
    path.pop()


#  matrix size
rows = int(input())
cols = int(input())

# create list for matrix
matrix = []

# fill the matrix from input
for _ in range(rows):
    matrix.append(list(input()))

all_paths(0, 0, matrix, "", [])
