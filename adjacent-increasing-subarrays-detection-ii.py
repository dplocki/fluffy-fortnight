class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        sub_array_length = 1
        sub_array_lengths = []

        for a, b in zip(nums, nums[1:]):
            if a < b:
                sub_array_length += 1
            else:
                sub_array_lengths.append(sub_array_length)
                sub_array_length = 1

        sub_array_lengths.append(sub_array_length)

        if len(sub_array_lengths) == 1:
            return sub_array_lengths[0] // 2

        return max(
            max(min(a, b), a // 2, b // 2)
            for a, b in zip(sub_array_lengths, sub_array_lengths[1:])
        )
