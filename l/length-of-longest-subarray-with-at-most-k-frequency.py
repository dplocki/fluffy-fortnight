class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        result = 0
        start = -1
        frequencies = defaultdict(int)

        for end, num in enumerate(nums):
            frequencies[num] += 1
            
            while frequencies[num] > k:
                start += 1
                frequencies[nums[start]] -= 1

            result = max(result, end - start)

        return result
