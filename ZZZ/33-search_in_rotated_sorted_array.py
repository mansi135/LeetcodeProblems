
def search(nums, target):

    p = find_pivot_point(nums, 0, len(nums) - 1)
    print(p)
    index = find_index(nums, 0, len(nums) - 1, target, p)

    return index


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


def find_index(arr, start, end, target, p):

    if p == -1 or start > end:
        return -1

    mid = int((start + end) / 2)
    l = len(arr)
    pivot_mid = (mid + p) % l

    if arr[pivot_mid] == target:
        return pivot_mid

    elif arr[pivot_mid] < target:
        start = mid + 1
        return find_index(arr, start, end, target, p)

    elif arr[pivot_mid] > target:
        end = mid - 1
        return find_index(arr, start, end, target, p)



print(search([1, 3], 0))
