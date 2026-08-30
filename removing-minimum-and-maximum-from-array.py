class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        minium_index, minimum = 0, nums[0]
        maximum_index, maximum = 0, nums[0]
        left, right = 0, 0
        n = 0

        for index, num in enumerate(nums):
            if minimum > num:
                minium_index = index
                minimum = num

            if maximum < num:
                maximum_index = index
                maximum = num

            if minium_index < maximum_index:
                left = minium_index
                right = maximum_index
            else:
                left = maximum_index
                right = minium_index

            n += 1

        return min(
            right + 1, # both from left
            n - left,  # both from right
            (left + 1) + (n - right)
        )
