class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        before_count = 0
        target_count = 0

        for num in nums:
            if num > target:
                continue
            
            if num == target:
                target_count += 1
                continue

            before_count += 1

        return list(range(before_count, before_count + target_count))
