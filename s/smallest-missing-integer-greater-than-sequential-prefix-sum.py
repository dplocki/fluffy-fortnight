class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        prefix_sum = nums[0]

        for a, b in pairwise(nums):
            if a + 1 == b:
                prefix_sum += b
            else:
                break

        set_nums = set(nums)

        for x in count(prefix_sum):
            if x not in set_nums:
                return x
