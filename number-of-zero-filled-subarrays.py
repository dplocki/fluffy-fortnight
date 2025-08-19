class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        result = 0
        zeros_len = 0

        for num in nums:
            if num == 0:
                zeros_len += 1
                result += zeros_len
            else:
                zeros_len = 0

        return result
