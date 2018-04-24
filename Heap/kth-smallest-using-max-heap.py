# To find kth smallest element in an array:
# Method 1- sort an index - k : complexity -> nlogn
#
#
# max - heap knowing/getting - O(1)
# removing - logn
# adding - logn
#
# Method 2- using max heap
#
# step 1- first make a heap of k elements - klogk
#
# if heap.size < k:           # klogk
#     heap.add(n[i])
#
# else if heap.max() > n[i]:  #(n-k)logk
#     heap.pop()
#     heap.add(n[i])
#
#     total = nlogk


import heapq

def kthsmallest(nums, k):
    heap = []

    i = 0
    while len(heap) < k:
        heapq.heappush(heap, nums[i])
        i += 1

    heapq._heapify_max(heap)

    while i < len(nums):
        print(heap, i)
        if heap[0] > nums[i]:
            heapq.heappop(heap)
            heapq.heappush(heap, nums[i])
            heapq._heapify_max(heap)
        i += 1

    # print(heap)

    return heap[0]

print(kthsmallest([4,0,3,2], 2))