class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        result = 0
        nums.sort()
        max_nums = len(nums)

        for first_side in range(max_nums - 2):
            for second_side in range(first_side + 1, max_nums - 1):
                limit = nums[first_side] + nums[second_side]
                third_side = bisect_left(nums, limit, lo=second_side + 1)
                result += third_side - 1 - second_side

        return result
