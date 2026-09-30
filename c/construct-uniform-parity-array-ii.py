class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        minimum = nums1[0]
        has_odd = False

        for num in nums1:
            if num < minimum:
                minimum = num
            if num % 2 == 1:
                has_odd = True

        if minimum % 2 == 1:
            return True

        return not has_odd
