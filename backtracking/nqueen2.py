"""
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return the number of distinct solutions to the n-queens puzzle.

Example 1:

Input: n = 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown.

Example 2:

Input: n = 1
Output: 1

Time Complexity: O(N!)
Auxiliary Space: O(N)

First queen has n possibilities (n cols) to be placed in row 1
Second queen has n - 1 possibilities to be placed in row 2
Third queen has n - 2 possibilities to be placed in row 3
...
...
T: n*(n-1)*(n-2) ....1 = O(n!)
"""


def total_nQueens(n):
    """
    :type n: int
    :rtype: int
    """
    if n == 1:
        return 1
    start = 0
    result = [0]
    pdia = set() # value remain same in positive diagonal
    ndia = set() # value remain same in negative diagonal
    cols = set()

    """
    ndia:
    for center dia r - c = 0, for one right to center dia r - c = 1 etc
    so if Q is placed at 0, 0 then will say center dia is occupied and will put 0 in ndia
    if Q is placed at 0, 1 then will say one rright to center dia is occupied and will put 1 in ndia etc
    [    0   1  2  3
      0  [0, 1, x, x],
      1  [x, 0, 1, x],
      2  [x, x, 0, 1],
      3  [x, x, x, 0],
    ]

    similar fo pdia, for pdia r + c is constant     
    """

    def solve(start, n, result, cols, pdia, ndia):
        if start == n:
            result[0] += 1
            return

        for c in range(n):
            if c in cols or start + c in pdia or start - c in ndia:
                continue
            cols.add(c)
            pdia.add(start + c)
            ndia.add(start - c)

            solve(start + 1, n, result, cols, pdia, ndia)

            cols.remove(c)
            pdia.remove(start + c)
            ndia.remove(start - c)

    solve(0, n, result, cols, pdia, ndia)
    return result[0]


def main():
    print(total_nQueens(4))
    print(total_nQueens(8))


if __name__ == '__main__':
    main()