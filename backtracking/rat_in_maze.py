"""
Rat in maze problem.
Rat can travel U, D, R, L
Rat can't travel diagonal
Find all valid paths from 0, 0 to r - 1, c - 1

T: no. of nodes (i.e. no. of function calls) * work done by function
# no. of nodes = for each cell there are 4 choices =
# 4 + 4x4 + 4x4x4 + 4x4...nxn = O(4^nxm) i.e. 4 to the power nxm  because there are nxm cells
# work done of function = O(1)
# T: O(4^nxm)
"""


def find_paths(maze, row, col, result, path=[]):
    if row == len(maze) - 1 and col == len(maze[0]) - 1:
        result.append(path.copy())
        return

    # Mark the current cell as visited
    maze[row][col] = 0

    # Explore all 4 directions from current cell
    directions = [('U', -1, 0), ('D', 1, 0), ('L', 0, -1), ('R', 0, 1)]
    for dir, r, c in directions:
        new_row = row + r
        new_col = col + c
        if new_row < len(maze) and new_col < len(maze[0]) and maze[new_row][new_col] == 1:
            path.append(dir)
            find_paths(maze, new_row, new_col, result)
            path.pop()

    #  unvisited the current cell
    maze[row][col] = 1


def find_paths2(maze, row, col, result, path=[]):
    if row == len(maze) or col == len(maze[0]) or maze[row][col] == 0:
        return

    # Mark the current cell as visited
    maze[row][col] = 0

    if row == len(maze) - 1 and col == len(maze[0]) - 1:
        result.append(path.copy())

    path.append("U")
    find_paths(maze, row - 1, col, result)
    path.pop()

    path.append("D")
    find_paths(maze, row + 1, col, result)
    path.pop()

    path.append("L")
    find_paths(maze, row, col - 1, result)
    path.pop()

    path.append("R")
    find_paths(maze, row, col + 1, result)
    path.pop()

    #  unvisited the current cell
    maze[row][col] = 1


def main():
    maze = [
        [1, 0, 0, 0],
        [1, 1, 0, 1],
        [1, 1, 0, 0],
        [0, 1, 1, 1]
    ]

    row = 0
    col = 0
    result = []
    find_paths(maze, row, col, result)
    print(result)


if __name__ == "__main__":
    main()