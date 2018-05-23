"""
You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water. Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells). The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

Example:

[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Answer: 16
Explanation: The perimeter is the 16 yellow stripes in the image below:

"""


class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        n = len(grid)
        m = len(grid[0])

        p = 0
        for r in range(n):
            for c in range(m):
                if grid[r][c] == 1:
                    if r - 1 == -1 or grid[r - 1][c] == 0:
                        p += 1
                    if c - 1 == -1 or grid[r][c - 1] == 0:
                        p += 1
                    if r + 1 == n or grid[r + 1][c] == 0:
                        p += 1
                    if c + 1 == m or grid[r][c + 1] == 0:
                        p += 1

        return p



