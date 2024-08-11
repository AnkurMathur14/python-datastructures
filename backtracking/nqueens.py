"""
51. N-Queens

The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

The idea is to place queens one by one in different rows, starting from the top row and leftmost column.
When we place a queen in a column, we check for clashes with already placed queens.
In the current row, if we find a col for which there is no clash, we mark this row and column as part of the solution
If we do not find such a row due to clashes, then we backtrack and return false.
i.e. Q1 in row1. Q2 in row2....

Time Complexity: O(N!)
Auxiliary Space: O(N)

First queen has n possibilities (n cols) to be placed in row 1
Second queen has n - 1 possibilities to be placed in row 2
Third queen has n - 2 possibilities to be placed in row 3
...
...
T: n*(n-1)*(n-2) ....1 = O(n!)
"""

"""
negative diagonal:
for center dia r - c = 0, for one right to center dia r - c = 1 etc
so if Q is placed at 0, 0 then will say center dia is occupied and will put 0 in ndia
if Q is placed at 0, 1 then will say one rright to center dia is occupied and will put 1 in ndia etc
[    0   1   2   3
  0  [0, 1, -2, x],
  1  [-1, 0, 1, -2],
  2  [-2, -1, 0, 1],
  3  [x, -2, -1, 0],
]

similar fo pdia, for pdia r + c is constant

[    0   1  2  3
  0  [0, 2, 4, 6],
  1  [2, 4, 6, 4],
  2  [4, 6, 4, 5],
  3  [6, 4, 5, 0],
]   
"""


def backtrack(r, n, board, result, col, p_dia, n_dia):
    if r == n:
        result.append(["".join(row) for row in board])
        return

    for c in range(n):
        if c in col or (r - c) in n_dia or (r + c) in p_dia:
            continue

        board[r][c] = 'Q'
        col.add(c)
        p_dia.add(r + c)
        n_dia.add(r - c)

        backtrack(r + 1, n, board, result, col, p_dia, n_dia)

        board[r][c] = '.'
        col.remove(c)
        p_dia.remove(r + c)
        n_dia.remove(r - c)


# Method 2
def solve_n_queens(n):
    col = set()  # Columns
    p_dia = set()  # Positive diagonal
    n_dia = set()  # Negative diagonal
    result = []
    board = [['.' for _ in range(n)] for _ in range(n)]

    backtrack(0, n, board, result, col, p_dia, n_dia)
    return result


def _solve_n_queens2(start, n, board, result):
    if start == n:
        result.append(["".join(row) for row in board])
        return

    def is_safe(row, col):

        # Check in same column
        for r in range(row - 1, -1, -1):
            if board[r][col] == 'Q':
                return False

        # Check in negative diagonal
        c = col - 1
        for r in range(row - 1, -1, -1):
            if c >= 0 and board[r][c] == 'Q':
                return False
            c -= 1

        # Check in positive diagonal
        c = col + 1
        for r in range(row - 1, -1, -1):
            if c < n and board[r][c] == 'Q':
                return False
            c += 1

        return True

    for c in range(n):
        if is_safe(start, c):
            board[start][c] = 'Q'
            _solve_n_queens2(start + 1, n, board, result)
            board[start][c] = '.'


def solve_n_queens2(n):
    board = [['.' for _ in range(n)] for _ in range(n)]
    start = 0
    result = []
    # start is same as row, we will start by placing first queen in row 0
    _solve_n_queens2(start, n, board, result)
    return result


def main():
    print(solve_n_queens(2))
    print(solve_n_queens2(4))


"""
[
    ['.Q..', '...Q', 'Q...', '..Q.'],
    ['..Q.', 'Q...', '...Q', '.Q..']
]
"""
if __name__ == '__main__':
    main()
