"""
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells,
where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

# T: O(M * N * 4^l)
# M = no of rows, N = no. of cols, l = avg len of each word
"""


def dfs(r, c, board, word, start, visited):

    if start >= len(word):
        return False
    if r < 0 or c < 0 or r >= len(board) or c >= len(board[0]) or (r, c) in visited or board[r][c] != word[start]:
        return
    if start == len(word) - 1:
        return True

    # Start visiting the cell
    visited.add((r, c))

    # Process all its neighbours
    ret = dfs(r+1, c, board, word, start + 1, visited) or \
    dfs(r-1, c, board, word, start + 1, visited) or \
    dfs(r, c+1, board, word, start + 1, visited) or \
    dfs(r, c-1, board, word, start + 1, visited)
    if ret:
        return True

    # Done visiting the cell
    visited.remove((r, c))
    return False


def word_search_1(board, word):
    ROW = len(board)
    COL = len(board[0])
    visited = set()
    for r in range(ROW):
        for c in range(COL):
            if dfs(r, c, board, word, 0, visited):
                return True
    return False


def main():
    board = [["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]]
    print(word_search_1(board, "oath"))
    return True


if __name__ == '__main__':
    main()

