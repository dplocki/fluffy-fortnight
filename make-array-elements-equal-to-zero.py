class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        all_sum = sum(nums)
        result = 0
        left_sum = 0

        for num in nums:
            if num != 0:
                left_sum += num
                continue

            right_sum = (all_sum - left_sum)
            if abs(right_sum - left_sum) == 1:
                result += 1
            elif right_sum == left_sum:
                result += 2

        return result
