#Tags - Backtracking , Matrix, Recursion , DFS
# Find the longest sequence of ones in a matrix

def exist(board):
    """
    :type board: List[List[str]]
    :type word: str
    :rtype: bool
    """

    if not board:
        return False

    r = len(board)
    c = len(board[0])

    max_len = 0

    for i in range(r):
        for j in range(c):
            visited = set()
            r = dfs(i, j, visited, board, 0)
            max_len = max(r, max_len)

    return max_len


def dfs(i, j, visited, board, curr):

    if (i, j) in visited or board[i][j] != 1:
        return 0

    curr += 1
    visited.add((i, j))

    my_max = []

    next_moves = {(1, 0), (-1, 0), (0, 1), (0, -1)}
    for n in next_moves:
        nexti = i + n[0]
        nextj = j + n[1]
        if is_valid_move(nexti, nextj, board):
            r = dfs(nexti, nextj, visited, board, curr)
            my_max.append(r)

    visited.remove((i, j))
    return max(curr, max(my_max))


def is_valid_move(i, j, board):
    if i < 0 or j < 0 or i == len(board) or j == len(board[0]):
        return False
    return True


m = [[1, 1, 1],
     [1, 0, 1],
     [1, 1, 0],
     [1, 0, 0]]

print(exist(m))
