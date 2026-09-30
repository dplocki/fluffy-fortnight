class Solution:
    def countCommas(self, n: int) -> int:
        tmp = n
        coma_group = -1

        while tmp:
            tmp //= 1_000
            coma_group += 1

        result = 0
        for index in range(coma_group, 0, -1):
            numbers_in_group = n - (1000 ** index - 1)
            result += numbers_in_group * index
            n -= numbers_in_group

        return result
