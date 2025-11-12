class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        limit = len(strs)
        main_set = [(s.count('0'), s.count('1')) for s in strs]

        @cache
        def internal(start: int, zeros_counter: int, ones_counter: int) -> int:
            if start >= limit:
                return 0

            result = internal(start + 1, zeros_counter, ones_counter)
            zeros, ones = main_set[start]
            if zeros_counter + zeros <= m and ones_counter + ones <= n:
                result = max(result, 1 + internal(start + 1, zeros_counter + zeros, ones_counter + ones))

            return result
        
        return internal(0, 0, 0)
