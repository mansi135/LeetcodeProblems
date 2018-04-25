def binary_search(arr,first,last,a):

    result="NotFound"

    if len(arr)==1:
        if a==arr[0]:
            result="Found"
    else:
        while(first<=last):
            mid=int((first+last)/2)
            if a==arr[mid]:
                result="Found"
                break
            elif a < arr[mid]:
                last=mid-1
                result=binary_search(arr,first,last,a)
            elif a > arr[mid]:
                first=mid+1
                result=binary_search(arr,first,last,a)
            else:
                result="Not Found"
    return result


# arr=[0,8,10,14,17]
# arr=[0,8]
arr=[8]
f=0
l=len(arr)-1
# print(binary_search(arr,f,l,18))

# Comments : In the above logic, i have written a while loop where I was intending an if condition since this while loop is never
# executed more than once.
# so refactor it to write an if condition


def binary_search_modified(arr, start, end, target):

    # if len(arr) == 1:
    #     if arr[0] == target:
    #         return 0
    #
    # if start > end:
    #     return -1

    # combining the above two conditions to one condition - nope!
    # l < r always works!!!

    if start > end:
        return -1

    # if start == end:
    #     if arr[start] == target:
    #         return start
    #     else:
    #         return -1

    mid = int((start + end) / 2)

    if arr[mid] == target:
        return mid

    elif arr[mid] < target:
        start = mid + 1
        return binary_search_modified(arr, start, end, target)

    elif arr[mid] > target:
        end = mid - 1
        return binary_search_modified(arr, start, end, target)


print(binary_search_modified(arr,f,l,7))
