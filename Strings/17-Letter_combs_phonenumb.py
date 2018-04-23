class Solution:

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        phone_map = {'2': ['a', 'b', 'c'],
                     '3': ['d', 'e', 'f'],
                     '4': ['g', 'h', 'i'],
                     '5': ['j', 'k', 'l'],
                     '6': ['m', 'n', 'o'],
                     '7': ['p', 'q', 'r', 's'],
                     '8': ['t', 'u', 'v'],
                     '9': ['w', 'x', 'y', 'z']
                     }

        split_digits = list(digits)
        r = self.recursive(split_digits, phone_map)

        return r

    def combinations(self, list1, list2):

        combined_list = []

        # O(n^2) ?
        for l1 in list1:
            for l2 in list2:
                combined_list.append(l1 + l2)

        return combined_list

    def recursive(self, split_digits, phone_map):

        if not split_digits:
            return []
        elif len(split_digits) == 1:
            return phone_map[split_digits[0]]
        elif len(split_digits) == 2:
            return self.combinations(phone_map[split_digits[0]], phone_map[split_digits[1]])

        return self.combinations(phone_map[split_digits[0]], self.recursive(split_digits[1:], phone_map))