# Find two indices i, j in the list (that may be the same) such that l[i] + l[j] == n
# Return that as a tuple

def find_two_nums_summing(l, n):
	t=()
	for i in range(len(l)):
		for j in range(i,len(l),1):
			if l[i]+l[j]==n:
				t+=(i,j)
	return t

#print(find_two_nums_summing([1,2,3,4,3],7))


x = [1,4,5,7,9,6,2]
# target = int(raw_input("Enter the number:"))
# for i in x:
#     if i < target:
#         pair = int(target) - int(i)
#         if pair in x:
#             print "the first number= %d the second number %d"%(i,pair)
#             break




# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#O(n)
def twoSum(nums, target):
	res = []
	dictMap = {}
	for i in range(len(nums)):
		nextNum = target - nums[i]
		if (nums[i] in dictMap):
			res.append([dictMap[nums[i]], i])
		else:
			dictMap[nextNum] = i

	return res

print(twoSum([2,3,2,3], 5))	# gives only unique indices, ideally it should have given (0,1) and (1,2)


# two sum if the given list is already sorted
# sorting O(nlogn)

def two_sum_sortedinp(nums, target):

	l = 0
	r = len(nums) - 1

	result = []

	while l < r:
		if nums[l] + nums[r] == target:
			result.append([l, r])
			l += 1
			r -= 1
		elif nums[l] + nums[r] < target:
			l += 1
		elif nums[l] + nums[r] > target:
			r -= 1


	return result

#print(two_sum_sortedinp([-2,-1,1,2,4,7,9], 0))

# just return unique combination of numbers, not indices - even this is wrong
def two_sum_hashmap(nums, target):

	map = {}
	result = set()

	for i,num in enumerate(nums):
		map[num] = map.get(num, []) + [i]

	for num in nums:
		if target-num in map:
			result.add((num, target-num))

	return result

# print(list(two_sum_hashmap([2,-2,2,2,-3,3,-3,3], 0)))
#print(list(two_sum_hashmap([2], 4)))