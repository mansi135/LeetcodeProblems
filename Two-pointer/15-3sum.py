# find three number whose sum is equal to zero
# two-pointer approach

def three_sum(nums):

    result = []

    if len(nums) < 3:
        return result

    nums.sort()

    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        l = i + 1
        r = len(nums) - 1
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            if s < 0:
                l += 1
            elif s > 0:
                r -= 1
            else:
                result.append([nums[i], nums[l], nums[r]])
                while l < r and nums[l] == nums[l+1]:
                    l += 1
                while l < r and nums[r] == nums[r-1]:
                    r -= 1
                l += 1
                r -= 1

    return result

r = three_sum([-1, 0, 1, 0, 1, 2, -1, -4])

#-4,-1,-1,0,0,1,2

print(r)







# Wrong approach:


class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        final_result = []

        for i, num in enumerate(nums):
            target = 0 - num
            partial_results = self.twoSum(nums[:i] + nums[i + 1:], target, num)
            final_result += partial_results

        return final_result

    def twoSum(self, nums, target, fnum):

        my_dict = {}
        result = []

        for num in nums:
            num_c = target - num
            if num in my_dict:
                b = [fnum, my_dict[num], num]
                b.sort()
                result.append(b)
            else:
                my_dict[num_c] = num
        return result