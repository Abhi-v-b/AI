def is_safe(board, row, col):
    # Check if it is safe to place a queen at the given position
    # Check row and column
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal
    i = row
    j = col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check lower diagonal
    i = row
    j = col
    while i < len(board) and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True


def solve_n_queens(board, col, solutions):
    n = len(board)

    # Base case: All queens are placed
    if col >= n:
        solutions.append([[1 if cell == 1 else 0 for cell in row] for row in board])
        return

    # Iterate over each row in the current column
    for row in range(n):
        if is_safe(board, row, col):
            # Place the queen in the current position
            board[row][col] = 1

            # Recursively solve for the next column
            solve_n_queens(board, col + 1, solutions)

            # Backtrack: Remove the queen from the current position
            board[row][col] = 0


def solve_nqueens(n):
    board = [[0] * n for _ in range(n)]
    solutions = []

    solve_n_queens(board, 0, solutions)

    return solutions


# Test the function
n = int(input("Enter the value of n: "))

solutions = solve_nqueens(n)
print(f"Number of solutions for {n}-queens problem: {len(solutions)}")
for solution in solutions:
    for row in solution:
        print(" ".join(str(cell) for cell in row))
    print()
