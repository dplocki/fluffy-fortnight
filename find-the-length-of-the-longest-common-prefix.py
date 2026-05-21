class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        prefixes_1, prefixes_2 = set(), set()

        for num in arr1:
            while num > 0:
                if num in prefixes_1:
                    break

                prefixes_1.add(num)
                num //= 10

        for num in arr2:
            while num > 0:
                if num in prefixes_2:
                    break
                    
                prefixes_2.add(num)
                num //= 10

        prefixes = prefixes_1 & prefixes_2
        if not prefixes:
            return 0

        return len(str(max(prefixes)))
