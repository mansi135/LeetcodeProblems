# This problem is also solved via recursion and memoization in that section (called top-down)

"""
using Tabulation
write 1st and 2nd strings orthogonal to each other
fill matrix with zeros
if last char of str1 == last char of str2:
    len_of_lcs = 1 + diagonally previous
else:
    len_of_lcs = max(left, up)

"""


# Dynamic Programming implementation of LCS problem - code courtesy:  from geeksforgeeks

def lcs(X, Y):
    # find the length of the strings
    m = len(X)
    n = len(Y)

    # declaring the array for storing the dp values
    L = [[None] * (n + 1) for i in range(m + 1)]

    """Following steps build L[m+1][n+1] in bottom up fashion
    Note: L[i][j] contains length of LCS of X[0..i-1]
    and Y[0..j-1]"""
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif X[i - 1] == Y[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])

    # L[m][n] contains the length of LCS of X[0..n-1] & Y[0..m-1]
    return L[m][n]
# end of function lcs