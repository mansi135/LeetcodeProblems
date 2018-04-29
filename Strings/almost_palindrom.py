# Write a function that accepts one bit of error in a palindrome


def palindrome_err(string):

    l = 0
    r = len(string) - 1

    while l < r:
        if string[l] != string[r]:
            return is_palindrome(string, l, r - 1) or is_palindrome(string, l + 1, r)
        l += 1
        r -= 1

    return True

# passing left and right pointers here to avoid list slicing , otherwise space complexity increases
def is_palindrome(string, l, r):

    while l < r:
        if string[l] != string[r]:
            return False
        l += 1
        r -= 1

    return True


print(palindrome_err('axxbccba'))
print(palindrome_err('axbccba'))
print(palindrome_err('abccba'))