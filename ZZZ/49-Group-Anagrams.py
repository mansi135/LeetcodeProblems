def groupAnagrams(strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """

    groups = []
    used = set()

# O(n^2)
    for i in range(len(strs)):
        if strs[i] not in used:
            new_group = [strs[i]]
            for j in range(i + 1, len(strs)):
                if sorted(strs[i]) == sorted(strs[j]): # condition for anagram
                    new_group.append(strs[j])
                    used.add(strs[j])
            groups.append(new_group)


    return groups

print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))


def alternate(strs):


    my_dict = {}

    for i in range(len(strs)):
        k = str(sorted(strs[i]))
        my_dict[k] = my_dict.get(k, []) + [strs[i]]

    return list(my_dict.values())

print(alternate(["eat", "tea", "tan", "ate", "nat", "bat"]))
