#imagine you have a robot and an NxN matrix. the robot can understand 2 instructions -- move one step to the right, and move one step down.
# write a function to determine how many unique paths the robot can take from the top left corner of the matrix to the bottom right corner

# Note that in this exercise, there are cases where I hit the same function with same inputs again (if the path is through
# same node) , hence its better to memoize

memoized_results = {}


def robot_paths(n, m):
    num_of_paths = helper(0,0,n,m)
    print(num_of_paths)


def helper(r,c,n,m):

    if r >= n or c >= m:
        return 0

    if r == n-1 and c == m-2 or r == n-2 and c == m-1:
        return 1

    # else:
    #     return helper(r + 1, c, n, m) + helper(r, c + 1, n, m)    #non-memoized version

    else:
        print(memoized_results)
        if (r+1, c) in memoized_results:
            row = memoized_results[(r+1, c)]
        else:
            row = helper(r+1, c, n, m)
            memoized_results[(r+1, c)] = row

        if (r, c+1) in memoized_results:
            col = memoized_results[(r, c+1)]
        else:
            col = helper(r, c+1, n, m)
            memoized_results[(r, c+1)] = col

        return row + col
        # like fibonacci - so inefficient - use memoize


#robot_paths(3,4)

# memoized_helper: Looks up, otherwise calls the "helper" and memoizes
# helper: Does the actual computation, only called by the memoized_helper
#
# Top level method, and the recursion calls into memoized_helper.



# Second similar problem -  design an algorithm to find a path for robot from top left to bottom right

def a_robot_path(n, m):
    path = []
    r = helper(0,0,n,m, path)
    if r:
        return path
    else:
        return None


def helper(r, c, n, m, path):

    if r >= n or c >= m:
        return False

    if r == n-1 and c == m-1:
        path.append((r, c))
        return True

    else:
        path.append((r, c))
        return helper(r+1, c, n, m, path) or helper(r, c+1, n, m, path)    #non-memoized version

print(a_robot_path(4,4))
