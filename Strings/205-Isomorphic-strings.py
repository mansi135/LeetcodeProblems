class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if len(s) != len(t):
            return False

        hash_map = {}

        visited = set()

        for i in range(len(s)):
            v = hash_map.get(s[i])
            if v is None:
                if t[i] not in visited:
                    hash_map[s[i]] = t[i]
                    visited.add(t[i])
                else:
                    return False
            elif t[i] != v:
                return False

        return True