#Tags - Backtracking , Matrix, Recursion , DFS

# This trick was helpful in 4 problems ->
'''
1) word serch
2) longest 1s
3) finding paths in directed graphs
4) finding all paths in binary tree
'''

class Solution(object):

    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        if not board:
            return False

        r = len(board)
        c = len(board[0])

        for i in range(r):
            for j in range(c):
                visited = set()
                if self.dfs(i, j, 0, visited, board, word):
                    return True

        return False

    def dfs(self, i, j, k, visited, board, word):

        if (i, j) in visited or board[i][j] != word[k]:
            return False

        if len(word) == k + 1:
            return True

        visited.add((i, j))

        next_moves = {(1, 0), (-1, 0), (0, 1), (0, -1)}
        for n in next_moves:
            nexti = i + n[0]
            nextj = j + n[1]
            if self.is_valid_move(nexti, nextj, board) and self.dfs(nexti, nextj, k + 1, visited, board, word):
                return True
        visited.remove((i, j))
        return False

    def is_valid_move(self, i, j, board):
        if i < 0 or j < 0 or i == len(board) or j == len(board[0]):
            return False
        return True


