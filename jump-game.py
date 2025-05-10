class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last_index = len(nums) - 1
        result = { last_index: True }

        for index in range(last_index - 1, -1, -1):
            result[index] = any(
                result.get(i + 1, False)
                for i in range(index, index + nums[index])
            )

        return result.get(0, False)
