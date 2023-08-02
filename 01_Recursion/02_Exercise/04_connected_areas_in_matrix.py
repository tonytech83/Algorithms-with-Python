class Area:
    def __init__(self, row, col, size):
        self.row = row
        self.col = col
        self.size = size


def find_area(row, col, matrix):
    if row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix[0]):
        return 0

    if matrix[row][col] != EMPTY:
        return 0

    matrix[row][col] = VISITED
    result = 1

    result += find_area(row - 1, col, matrix)  # down
    result += find_area(row + 1, col, matrix)  # up
    result += find_area(row, col + 1, matrix)  # right
    result += find_area(row, col - 1, matrix)  # left

    return result


rows = int(input())
cols = int(input())

matrix = [[x for x in input()] for _ in range(rows)]
EMPTY, WALL, VISITED = '-', '*', 'v'

# List of tuples to store founded areas
areas = []

for row in range(rows):
    for col in range(cols):
        size = find_area(row, col, matrix)
        if size:
            areas.append(Area(row, col, size))

print(f'Total areas found: {len(areas)}')
for idx, area in enumerate(sorted(areas, key=lambda t: (-t.size, t.row, t.col))):
    print(f'Area #{idx + 1} at ({area.row}, {area.col}), size: {area.size}')
