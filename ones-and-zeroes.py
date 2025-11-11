class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        limit = len(strs)
        main_set = [(s.count('0'), s.count('1')) for s in strs]

        @cache
        def internal(start: int, zeros_counter: int, ones_counter: int) -> int:
            if start >= limit:
                return 0

            result = 0
            for index in range(start, limit):
                zeros, ones = main_set[index]

                tmp_zeros_counter = zeros_counter + zeros
                tmp_ones_counter = ones_counter + ones

                if tmp_zeros_counter > m or tmp_ones_counter > n:
                    continue

                result = max(result, 1 + internal(index + 1, tmp_zeros_counter, tmp_ones_counter))

            return result
        
        return internal(0, 0, 0)
