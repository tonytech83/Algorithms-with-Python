# exam: 05. Paths in Labyrinth
# judge: https://judge.softuni.org/Contests/Compete/Index/3459#4


def is_candidate(row, col, lab):
    if row < 0 or row >= len(lab) or col < 0 or col >= len(lab[0]):
        return False

    if lab[row][col] == VISITED:
        return False

    if lab[row][col] == WALL:
        return False

    return True


def find_all_paths(row, col, lab, direction, path):
    if not is_candidate(row, col, lab):
        return

    if lab[row][col] == EXIT:
        path.append(direction)
        print(''.join(path))
        path.pop()
        return

        # Pre-action
    lab[row][col] = VISITED
    path.append(direction)

    # Recursion calls
    find_all_paths(row, col - 1, lab, 'L', path)
    find_all_paths(row, col + 1, lab, 'R', path)
    find_all_paths(row - 1, col, lab, 'U', path)
    find_all_paths(row + 1, col, lab, 'D', path)

    # Post-action
    path.pop()
    lab[row][col] = EMPTY


EMPTY, EXIT, VISITED, WALL = '-', 'e', 'v', '*'
rows = int(input())
cols = int(input())

matrix = [[x for x in input()] for row in range(rows)]

find_all_paths(0, 0, matrix, '', [])
