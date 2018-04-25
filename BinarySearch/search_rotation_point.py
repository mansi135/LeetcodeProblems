#given a sorted , rotated array, find the rotation point
#Hint-if mid element is less than last, rotation point is in left half, else its in right half

def search_rotation(arr,first,last):
    while(first<=last):
        mid=int((first+last)/2)
        if arr[mid] < arr[mid+1] and arr[mid] < arr[mid-1]:
            rot_point=arr[mid]
            break
        elif arr[mid]<arr[last]:
            last=mid-1
            rot_point=search_rotation(arr,first,last)
        elif arr[mid]>arr[last]:
            first=mid+1
            rot_point=search_rotation(arr,first,last,)
    return rot_point

# arr=[24,7,10,18,19,20]
# arr=[0,1]
# arr=[2,1]

# are duplicates allowed ?
# arr = [7, 7, 7]
# arr = [24, 7, 7]
# arr = [25, 25, 7]
# arr = [1, 3]
arr = [5]

f=0
l=len(arr)-1
# print(search_rotation(arr,f,l))

def find_pivot_point(arr, start, end):

    if start > end:
        pivot = -1

    elif start == end:
        pivot = start

    else:

        mid = int((start + end) / 2)

        if arr[mid] < arr[mid + 1] and arr[mid] < arr[mid - 1]:
            pivot = mid

        elif arr[mid] <= arr[end]:
            end = mid - 1
            pivot = find_pivot_point(arr, start, end)

        elif arr[mid] > arr[end]:
            start = mid + 1
            pivot = find_pivot_point(arr, start, end)

    return pivot


print(find_pivot_point(arr,f,l))