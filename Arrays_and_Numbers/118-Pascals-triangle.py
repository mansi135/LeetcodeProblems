class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []

        triangle = [[1]]

        for r in range(1, numRows):
            # prev = 0
            # last = 0
            new_row = [1]
            for c in range(r - 1):
                new_row.append(triangle[r - 1][c] + triangle[r - 1][c + 1])
            new_row.append(1)
            triangle.append(new_row)

        return triangle
