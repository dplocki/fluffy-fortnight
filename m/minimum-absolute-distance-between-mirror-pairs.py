class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        dp = {}
        result = inf

        for index, num in enumerate(nums):
            if num in dp:
                result = min(index - dp[num], result)

            dp[self.reverse_number(num)] = index

        return result if result != inf else -1

    def reverse_number(self, num: int) -> int:
        result = 0

        while num:
            digit = num % 10

            result *= 10
            result += digit

            num //= 10
    
        return result
