class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        minium, maksimum = nums[0], nums[0]
        for num in nums:
            if num < minium:
                minium = num
            if num > maksimum:
                maksimum = num

        return (maksimum - minium) * k
