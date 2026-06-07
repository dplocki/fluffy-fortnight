class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        
        def internal(num: int) -> int:
            if num < 100:
                return 0

            num_as_string = str(num)

            @cache
            def dfs(index: int, a: int, b: int, tight: bool, started: bool, length: int) -> Tuple[int, int]:
                if index == len(num_as_string):
                    return (1, 0)

                limit = int(num_as_string[index]) if tight else 9
                current, waves = 0, 0

                for digit in range(0, limit + 1):
                    new_tight = tight and digit == int(num_as_string[index])
                    new_started = started or digit > 0
                    new_len = (length + 1) if new_started else 0

                    c, w = dfs(index + 1, b, digit, new_tight, new_started, new_len)

                    if length > 1 and (a < b > digit or a > b < digit):
                        w += c

                    current += c
                    waves += w

                return current, waves

            return dfs(0, 0, 0, True, False, 0)[1]

        return internal(num2) - internal(num1 - 1)
