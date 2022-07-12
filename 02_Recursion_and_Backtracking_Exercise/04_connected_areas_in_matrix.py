class Area:
    def __init__(self, row, col, size):
        self.row = row
        self.col = col
        self.size = size


def find_areas(row, col, matrix):
    # check is outside of matrix
    if row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0]):
        return 0
    # check for wall of area
    if matrix[row][col] != "-":
        return 0
    # mark visited cells
    matrix[row][col] = "v"

    result = 1
    result += find_areas(row - 1, col, matrix)
    result += find_areas(row + 1, col, matrix)
    result += find_areas(row, col - 1, matrix)
    result += find_areas(row, col + 1, matrix)

    return result


rows = int(input())
cols = int(input())

# create list for matrix
matrix = []

# fill the matrix from input
for _ in range(rows):
    matrix.append(list(input()))

# list to store the areas
areas = []

# walk through all cells of matrix
for row in range(rows):
    for col in range(cols):
        size = find_areas(row, col, matrix)
        if size == 0:
            continue
        areas.append(Area(row, col, size))

print(f"Total areas found: {len(areas)}")
for idx, area in enumerate(sorted(areas, key=lambda a: a.size, reverse=True)):
    print(f"Area #{idx + 1} at ({area.row}, {area.col}), size: {area.size}")
