class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        return list(sorted(set(range(min(nums), max(nums) + 1)) - set(nums)))
