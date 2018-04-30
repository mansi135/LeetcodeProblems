#class Solution(object):

def longest_substr(str):
    if len(str) <= 1:
        return len(str)
    i = 0
    #substr = str[0]
    #leng = len(substr)
    #longest = substr
    leng = 0
    while i != len(str):
        substr = str[i:i+1]
        longest = substr
        j = i+1
        while j != len(str) and str[j] not in substr:
            substr += str[j]
            j = j+1
        if len(substr) > leng:  # leng = max(leng,len(substr))
            leng = len(substr)
            longest = substr
        i = i+1

    #return longest
    return leng

print(longest_substr('pwwkew'))

# if __name__ == "__main__":
#     solution = Solution()



