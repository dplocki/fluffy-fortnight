class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        prev_sub_array_length, sub_array_length = 0, 1

        for i in range(0, len(nums) - 1):
            if nums[i] < nums[i + 1]:
                sub_array_length += 1
            else:
                prev_sub_array_length = sub_array_length
                sub_array_length = 1

            if prev_sub_array_length // 2 >= k or sub_array_length // 2 >= k or min(prev_sub_array_length, sub_array_length) >= k:
                return True

        return False
