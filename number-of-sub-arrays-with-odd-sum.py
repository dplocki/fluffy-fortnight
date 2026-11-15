MOD = (10 ** 9) + 7


class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        result = 0
        pre_odd = 0
        pre_even = 1
        pre_sum = 0

        for num in arr:
            pre_sum += num

            if pre_sum & 1 == 1:
                result += pre_even
                pre_odd += 1
            else:
                result += pre_odd
                pre_even += 1

        return result % MOD
