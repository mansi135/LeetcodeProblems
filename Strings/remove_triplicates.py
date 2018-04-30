# Given a string, remove all matches of 3 or more consecutive chars (Candy Crush style)
# -- i.e. ABBBCC - > ACC
# -- i.e. ABBCCCB -> A


def remove_triplicates(s):

    new_string = ""

    # Following code segmnt will not work since i+=3 is not allowed inside for loop in python
    # for i in range(len(s)-2):
    #     print(s[i])
    #     if s[i:i+3] == s[i] * 3:
    #         print(s[i:i+3])
    #         i += 3
    #     else:
    #         new_string += s[i]

    i = 0
    # Method-1
    # while i < len(s):
    #     if i < len(s)-2 and s[i:i+3] == s[i] * 3:
    #         i += 3
    #     else:
    #         new_string += s[i]
    #         i += 1

    # Method-2
    while i < len(s)-2:
        if s[i:i+3] == s[i] * 3:
            i += 3
        else:
            new_string += s[i]
            i += 1

    new_string += s[i:]

    if len(new_string) == len(s):
        return new_string
    else:
        return remove_triplicates(new_string)


print(remove_triplicates('ABBBCC'))
print(remove_triplicates('ABBCCCB'))