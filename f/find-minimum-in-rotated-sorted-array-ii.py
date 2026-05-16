class Solution:
    def findMin(self, nums: List[int]) -> int:
        def internal(left: int, right: int) -> int:
            if nums[left] < nums[right]:
                return nums[left]

            if left + 1 == right:
                return nums[right]

            middle = left + ((right - left) >> 1)
            return min(internal(left, middle), internal(middle, right))

        n = len(nums) - 1
        if n == 0:
            return nums[0]

        return internal(0, n)
