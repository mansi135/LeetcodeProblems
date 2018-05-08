#Given a collection of distinct numbers, return all possible permutations.
# Input: [1,2,3]
# Output:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]


class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        if len(nums) == 1:
            return [nums]

        perms = []

        for i in range(len(nums)):
            extra = nums[:i] + nums[i + 1:]
            result = self.permute(extra)
            for r in result:
                perms.append([nums[i]] + r)

        return perms


# Below code works for duplicates also - all possible string permutations
def permute(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """

    if len(nums) == 1:
        return [(nums[0],)]

    perms = set()

    for i in range(len(nums)):
        extra = nums[:i] + nums[i + 1:]
        result = permute(extra)
        # print(result)
        for r in result:
            # print(r)
            s = (nums[i],) + r
            perms.add(s)

    return perms


def main(string):
    s = list(string)
    print(permute(s))


main('AABC')

'''
Subset means 2^n (there can be empty sets also or sets with just 1 element
Permutation means length of each set is always n (it cnt be empty or 1) -> so its n!
If there are repeats -> n!/r1!*r2! etc
'''