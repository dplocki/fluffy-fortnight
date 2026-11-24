class Solution:
    def maxLength(self, nums: List[int]) -> int:
        result = 2
        substring_product = 1
        start = 0

        for end, num in enumerate(nums):
            while gcd(substring_product, num) > 1:
                substring_product //= nums[start]
                start += 1
            
            substring_product *= num
            result = max(result, end - start + 1)

        return result
