# exam: 06. 8 Queens Puzzle
# judge: https://judge.softuni.org/Contests/Compete/Index/3459#5

def print_board(board):
    [print(' '.join(row)) for row in board]
    print()


def can_set_queen(row, col, rows, cols, left_diagonals, right_diagonals):
    if all([row not in rows, col not in cols, (row - col) not in left_diagonals, (row + col) not in right_diagonals]):
        return True

    return False


def set_queen(row, col, board, rows, cols, left_diagonals, right_diagonals):
    board[row][col] = QUEEN
    rows.add(row)
    cols.add(col)
    left_diagonals.add(row - col)
    right_diagonals.add(row + col)


def remove_queen(row, col, board, rows, cols, left_diagonals, right_diagonals):
    board[row][col] = EMPTY
    rows.remove(row)
    cols.remove(col)
    left_diagonals.remove(row - col)
    right_diagonals.remove(row + col)


def position_queens(row, board, rows, cols, left_diagonals, right_diagonals):
    # BASE CASE
    if row == board_size:
        print_board(board)
        return

    for col in range(board_size):
        if can_set_queen(row, col, rows, cols, left_diagonals, right_diagonals):
            # Pre-action
            set_queen(row, col, board, rows, cols, left_diagonals, right_diagonals)
            # Recursive call
            position_queens(row + 1, board, rows, cols, left_diagonals, right_diagonals)
            # Post action
            remove_queen(row, col, board, rows, cols, left_diagonals, right_diagonals)


board_size = 8
EMPTY, QUEEN = '-', '*'
board = [[EMPTY] * board_size for _ in range(board_size)]

position_queens(0, board, set(), set(), set(), set())
