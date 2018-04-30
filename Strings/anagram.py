# Anagram - two words with rearrangement of same letters - use len of sorted
# Isogram - a word with no letters repeated - use len of set
# Biagram - two consecutive words

def ana(str1, str2):
    if sorted(str1) == sorted(str2):
        print("anagram")

    else:
        print("no not")


ana("mansi", "insami")


###########################################
# take second element for sort
def takeSecond(elem):
    return elem[1]

# random list
random = [(2, 2), (3, 4), (4, 1), (1, 3)]

# sort list with key
sortedList = sorted(random, key=takeSecond)

# print list
print('Sorted list:', sortedList)

###########################################
bytes = [0] * 5
print(bytes)

###########################################

p = 'mansi'
s = set([x for x in p])
s.add(1)
#s.add([x for x in p])   <- this will give an error because list is mutable , so what if we change the list later??
## we can add tuple rather , because tuple is immutable
print(s)

p1 = 'man'
s1 = set([x for x in p1])

print(s & s1)

print(type({'a': 1}.values()))