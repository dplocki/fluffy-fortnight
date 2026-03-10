class Solution:
    MOD = 10**9 + 7

    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:

        @cache
        def internal(zeros: int, ones: int, last_digit: int) -> int:
            if zeros == 0:
                return 1 if last_digit == 1 and ones <= limit else 0

            if ones == 0:
                return 1 if last_digit == 0 and zeros <= limit else 0

            if last_digit == 0:
                result = internal(zeros - 1, ones, 0) + internal(zeros - 1, ones, 1)
                if zeros - limit - 1 >= 0:
                    result -= internal(zeros - limit - 1, ones, 1)

                return result
            else:
                result = internal(zeros, ones - 1, 0) + internal(zeros, ones - 1, 1)

                if ones - limit - 1 >= 0:
                    result -= internal(zeros, ones - limit - 1, 0)

                return result
      
        result = (internal(zero, one, 0) + internal(zero, one, 1)) % Solution.MOD
        internal.cache_clear()
        return result
