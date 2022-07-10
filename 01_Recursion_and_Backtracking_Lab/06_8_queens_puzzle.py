def print_board(chess_board):
    for row in chess_board:
        print(" ".join(row))
    print()


def can_place_queen(row, col, rows, cols, left_diagonals, right_diagonals):
    if row in rows:
        return False
    if col in cols:
        return False
    if (row - col) in left_diagonals:
        return False
    if (row + col) in right_diagonals:
        return False
    return True


def set_queen(row, col, chess_board, rows, cols, left_diagonals, right_diagonals):
    chess_board[row][col] = "*"
    rows.add(row)
    cols.add(col)
    left_diagonals.add(row - col)
    right_diagonals.add(row + col)


def remove_queen(row, col, chess_board, rows, cols, left_diagonals, right_diagonals):
    chess_board[row][col] = "-"
    rows.remove(row)
    cols.remove(col)
    left_diagonals.remove(row - col)
    right_diagonals.remove(row + col)


def put_queens(row, chess_board, rows, cols, left_diagonals, right_diagonals):
    if row == 8:
        print_board(chess_board)
        return

    for col in range(8):
        if can_place_queen(row, col, rows, cols, left_diagonals, right_diagonals):
            # pre-action
            set_queen(row, col, chess_board, rows, cols, left_diagonals, right_diagonals)
            # recursive
            put_queens(row + 1, chess_board, rows, cols, left_diagonals, right_diagonals)
            # post-action
            remove_queen(row, col, chess_board, rows, cols, left_diagonals, right_diagonals)


n = 8
chess_board = []
[chess_board.append(["-"] * n) for _ in range(n)]

put_queens(0, chess_board, set(), set(), set(), set())
