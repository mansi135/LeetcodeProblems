#Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

#Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

# This solution os O(n^2)
class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) < 2:
            return len(nums)

        uniq_len = 1
        i = 1

        while i < len(nums):
            if nums[i] != nums[i - 1]:
                uniq_len += 1
                i += 1
            else:
                nums.pop(i)

        return uniq_len


#O(n):

        # whenvever we have to do in-place in array, use two pointers - O(n)

    def alternate(self, nums):
        output_index = 0
        input_index = 0
        prev = None

        while input_index < len(nums):
            if prev == None or nums[input_index] != prev:
                prev = nums[input_index]
                nums[output_index] = nums[input_index]
                output_index += 1
            input_index += 1

        return output_index

    def more_alternate(self, nums):

        if not nums:
            return 0

        output_index = 0

        for i in range(1, len(nums)):
            if nums[i] != nums[output_index]:
                output_index += 1
                nums[output_index] = nums[i]

        return output_index + 1

# def remove_3_candy(s):
#
#     s = list(s)
#
#     output_index = 0
#
#     for i in range(1, len(s)):
#         if s[i] == s[output_index]:
#             s[output_index] = s[]

# Similar question one more - remove elements in place:

#Given an array nums and a value val, remove all instances of that value in-place and return the new length.

#Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

#The order of elements can be changed. It doesn't matter what you leave beyond the new length.


class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        output_index = 0
        input_index = 0

        while input_index < len(nums):
            if nums[input_index] != val:
                nums[output_index] = nums[input_index]
                output_index += 1
            input_index += 1

        return output_index



# Remove duplicates in sorted LL :

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None

        tmp = head

        while tmp.next is not None:
            if tmp.val == tmp.next.val:
                tmp.next = tmp.next.next
            else:
                tmp = tmp.next

        return head
