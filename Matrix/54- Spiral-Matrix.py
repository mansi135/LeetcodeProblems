class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        if not matrix:
            return []

        result = []

        row_start = 0
        row_end = len(matrix) - 1

        col_start = 0
        col_end = len(matrix[0]) - 1

        while row_start <= row_end and col_start <= col_end:

            # print(result)

            # right
            for c in range(col_start, col_end + 1):
                result.append(matrix[row_start][c])

            row_start += 1

            # down
            for r in range(row_start, row_end + 1):
                result.append(matrix[r][col_end])

            col_end -= 1

            if row_start <= row_end:
                # left
                for c in range(col_end, col_start - 1, -1):
                    result.append(matrix[row_end][c])

            row_end -= 1

            if col_start <= col_end:
                # up
                for r in range(row_end, row_start - 1, -1):
                    result.append(matrix[r][col_start])

            col_start += 1

        return result

