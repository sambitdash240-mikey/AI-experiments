def print_board(board):
    for row in board:
        print(" ".join(row))


def is_safe(board, row, col, n):
    # 1. Check column above
    for i in range(row):
        if board[i][col] == 'Q':
            return False

    # 2. Check upper-left diagonal (\)
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1

    # 3. Check upper-right diagonal (/)
    i, j = row - 1, col + 1
    while i >= 0 and j < n:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j += 1

    return True


def solve(board, row, n):
    if row == n:
        return True

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 'Q'

            if solve(board, row + 1, n):
                return True

            board[row][col] = '.'  # Backtrack

    return False


# Main program
n = int(input("Enter the number of queens (N): "))
board = [['.' for _ in range(n)] for _ in range(n)]

if solve(board, 0, n):
    print("\nSolution for the problem:")
    print_board(board)
else:

    print("\nNo solution exists!")