class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        max_nums = len(nums)

        for i in range(len(nums) - 1, 1, -1):
            largest_side = nums[i]
            middle_side = nums[i - 1]
            shortest_side = nums[i - 2]

            if largest_side < middle_side + shortest_side:
                return shortest_side + middle_side + largest_side
        
        return 0
