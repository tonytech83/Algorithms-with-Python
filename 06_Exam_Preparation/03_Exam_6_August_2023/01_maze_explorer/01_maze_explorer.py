"""
exam: 01. Maze Explorer
judge: https://judge.softuni.org/Contests/Practice/Index/4044#0
"""


def read_maze():
    size = int(input())

    matrix = []
    start_pos = ()

    for row in range(size):
        matrix.append([x for x in input()])
        if START in matrix[row]:
            start_pos = (row, matrix[row].index(START))

    return matrix, start_pos


def is_valid_path(row, col, maze, visited):
    return 0 <= row < len(maze) and 0 <= col < len(maze) and maze[row][col] != WALL and not visited[row][col]


def find_shortest_path(start, maze, visited):
    row, col = start

    if maze[row][col] == DESTINATION:
        return 0

    visited[row][col] = True
    min_steps = float('inf')

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    for row_change, col_change in directions:
        new_row, new_col = row + row_change, col + col_change
        if is_valid_path(new_row, new_col, maze, visited):
            steps = find_shortest_path((new_row, new_col), maze, visited)
            min_steps = min(min_steps, steps + 1)

    visited[row][col] = False
    return min_steps


WALL, START, DESTINATION = '#', 'S', 'E'
maze, start = read_maze()

visited = [[False for _ in range(len(maze))] for _ in range(len(maze))]
path = find_shortest_path(start, maze, visited)

print(path)
