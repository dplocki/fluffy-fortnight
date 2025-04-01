class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        return list({
            tuple(sorted(combination))
            for combination in combinations(nums, 4)
            if sum(combination) == target
        })
