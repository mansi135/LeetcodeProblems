import itertools
import unittest

def get_center(matrix, n, m):
    """Get all possible centers"""

    n_half = int(n / 2)
    m_half = int(m / 2)

    # if odd number of rows/columns, then only one center, otherwise more centers possible
    # get all row centers
    if n % 2 != 0:
        row_center = [n_half]
    else:
        row_center = [n_half- 1, n_half]

    # get all column centers
    if m % 2 != 0:
        col_center = [m_half]
    else:
        col_center = [m_half - 1, m_half]

    # get a list of coordinates of all possible centers
    centers = list(itertools.product(row_center, col_center))

    # Since the rabbit doesn't have to choose between two points which are of same value,
    # the max function below will always select the first of the two equal values:

    # this variable stores max center value and also the coordinates of center
    center_values = max([(matrix[r][c], r, c) for r,c in centers], key = lambda x : x[0])

    return center_values


def main_function(matrix):
    """Main logic to decide next move and calculate total calories eaten"""

    # n = num of rows
    n = len(matrix)

    # m = num of columns
    m = len(matrix[0])

    max_val, row, col = get_center(matrix, n, m)

    calories_eaten = max_val

    # set the center to zero, since its eaten
    matrix[row][col] = 0

    next_move = []

    # check all 4 next possible moves (up, down ,left, right)
    # if next move is within boundary and is not zero, append it to next_move []
    # append (val, r, c)
    while True:
        if row + 1 != n and matrix[row+1][col] != 0:
            down = (matrix[row+1][col], row+1, col)
            next_move.append(down)
        if row - 1 >= 0 and matrix[row-1][col] != 0:
            up = (matrix[row-1][col], row-1, col)
            next_move.append(up)
        if col + 1 != m and matrix[row][col+1] != 0:
            right = (matrix[row][col+1], row, col+1)
            next_move.append(right)
        if col - 1 >= 0 and matrix[row][col-1] != 0:
            left = (matrix[row][col-1], row, col-1)
            next_move.append(left)

        # if there is no possible move, break and return
        if not next_move:
            break

        # get the max of all possible options
        next_val, row, col = max(next_move, key = lambda x : x[0])

        calories_eaten += next_val
        matrix[row][col] = 0
        next_move = []

    return calories_eaten



class MyTestCases(unittest.TestCase):

  def test_carrots1(self):

      my_matrix = [[5, 7, 8, 6, 3],
                   [0, 0, 7, 0, 4],
                   [4, 6, 3, 4, 9],
                   [3, 1, 0, 5, 8]]

      self.assertEqual(main_function(my_matrix), 27)

  def test_carrots2(self):

      my_matrix = [[0, 8, 8, 6],
                   [0, 0, 3, 0],
                   [4, 7, 7, 2],
                   [3, 1, 0, 9]]

      self.assertEqual(main_function(my_matrix), 33)


  def test_carrots3(self):

      my_matrix = [[5, 7],
                   [0, 0]]

      self.assertEqual(main_function(my_matrix), 12)


  def test_carrots4(self):

      my_matrix = [[8]]

      self.assertEqual(main_function(my_matrix), 8)



if __name__ == "__main__":

  unittest.main()


