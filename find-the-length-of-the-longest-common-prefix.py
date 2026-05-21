class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        prefixes_1, prefixes_2 = set(), set()

        for num in map(str, arr1):
            for i in range(len(num)):
                prefixes_1.add(num[:i + 1])

        for num in map(str, arr2):
            for i in range(len(num)):
                prefixes_2.add(num[:i + 1])

        return max(map(len, prefixes_1 & prefixes_2), default=0)
