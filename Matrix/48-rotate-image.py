class Solution(object):

    # This method has n^2 complexity
    def rotate_old_method(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        passes = 0
        n = len(matrix)

        while passes < int(n / 2):
            b = n - 2 * passes
            for i in range(0, b - 1):
                tmp = matrix[i + passes][passes]
                matrix[i + passes][passes] = matrix[b - 1 + passes][i + passes]
                matrix[b - 1 + passes][i + passes] = matrix[b - 1 + passes - i][b - 1 + passes]
                matrix[b - 1 + passes - i][b - 1 + passes] = matrix[passes][b - 1 - i + passes]
                matrix[passes][b - 1 - i + passes] = tmp
            passes += 1

    # rotate clockwise - transpose and flip n^2 + n
    def rotate(self, matrix):

        for r in range(len(matrix)):
            for c in range(r):
                tmp = matrix[r][c]
                matrix[r][c] = matrix[c][r]
                matrix[c][r] = tmp

        for r in range(len(matrix)):
            matrix[r].reverse()

    # rotate anticlockwise - flip and transpose