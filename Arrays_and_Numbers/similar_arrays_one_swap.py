# Two arrays are called similar if one can be obtained from another by swapping at most one pair of elements in one of the arrays.

# Two arrays are called similar if one can be obtained from another by swapping at most one pair of elements in one of the arrays.
#
# Given two arrays, check whether they are similar.
#
# Example
#
# For A = [1, 2, 3] and B = [1, 2, 3], the output should be areSimilar(A, B) = true.
#
# The arrays are equal, no need to swap any elements.
#
# For A = [1, 2, 3] and B = [2, 1, 3], the output should be areSimilar(A, B) = true.
#
# We can obtain B from A by swapping 2 and 1 in B.
#
# For A = [1, 2, 2] and B = [2, 1, 1], the output should be areSimilar(A, B) = false.
#
# Any swap of any two elements either in A or in B won't make A and B equal.


# O(n) space and O(n) time:

def check_similar(arr1, arr2):

    if len(arr1) != len(arr2):
        return False

    diff = []

    for i in range(len(arr1)):

        if arr1[i] != arr2[i]:
            diff.append(i)

            if len(diff) > 2:
                return False
            if len(diff) == 2:
                if arr1[diff[0]] != arr2[diff[1]] or arr1[diff[1]] != arr2[diff[0]]:
                    return False

    return len(diff) == 0 or len(diff) == 2


# function
# areSimilar(arr1, arr2)
# {
# if (arr1.length !== arr2.length)
# return false;
#
# let
# diff = []; // initialize
# array
# that
# 'll be used to track indices where values differ
#
# for (let i = 0; i < arr1.length; i++) { // loop thru first array
# if (arr1[i] != = arr2[i]) {// check for value differences between arrays at each index
# diff.push(i); // if the values differ push index into diff array
#
# if (diff.length > 2)
# return false;
#
# if (diff.length === 2) {
# // use the diff array indices to swap, if swapped pairs are not eqaul
# return false;
# if (arr1[diff[0]] !== arr2[diff[1]] | | arr1[diff[1]] != = arr2[diff[0]]) {
# return false;
# }
# }
# }
# }
# // if it makes it through all of that
# return diff.length === 0 | | diff.length == = 2;
# }