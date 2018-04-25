#binary search, also known as half-interval search,
# logarithmic search, or binary chop, is a search algorithm that finds the position of a target value within a sorted array

def binary_search(l,a):
    if len(l)==1:
        if a==l[0]:
            result="Found"
        else:
            result="Not Found"
    else:
        mid_elem=l[int(len(l)/2)]
        if a==mid_elem:
            result="Found"
        elif a < mid_elem:
            result=binary_search(l[:int(len(l)/2)],a)
        elif a > mid_elem:
            result=binary_search(l[int(len(l)/2):],a)
        else:
            result="Not Found"

    return result

print(binary_search([1,2,3,4,5,6],4))