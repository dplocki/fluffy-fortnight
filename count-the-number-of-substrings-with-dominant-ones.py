class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        ones_zeros = { -1: (0, 0) }
        ones = 0
        zeros = 0

        for index, d in enumerate(s):
            if d == '0':
                zeros += 1
            else:
                ones += 1

            ones_zeros[index] = (ones, zeros)

        n = ones + zeros
        result = 0

        for start in range(n):
            s_one, s_zero = ones_zeros[start - 1]
            for end in range(n):
                e_one, e_zero = ones_zeros[end]
                if (e_one - s_one) > 0 and (e_one - s_one) >= (e_zero - s_zero) ** 2:
                    result += 1

        return result
