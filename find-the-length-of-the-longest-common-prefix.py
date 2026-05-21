class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        prefixes = set()

        for num in arr1:
            while num > 0:
                if num in prefixes:
                    break

                prefixes.add(num)
                num //= 10

        the_longest_prefix = 0
        for num in arr2:
            while num > the_longest_prefix:
                if num in prefixes:
                    the_longest_prefix = num
                    break
            
                num //= 10
        
        if the_longest_prefix == 0:
            return 0

        return len(str(the_longest_prefix))
