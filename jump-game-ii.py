class Solution:
    def jump(self, nums: List[int]) -> int:
        last_index = len(nums) - 1
        near = index = jumps = 0

        while index < last_index:
            farthest = max(i + nums[i] for i in range(near, index + 1))
            near = index + 1
            index = farthest
            jumps += 1

        return jumps
