class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        
        @cache
        def internal(left: int, right: int) -> int:
            if left == right:
                return nums[left]

            return max(
                nums[left] - internal(left + 1, right),
                nums[right] - internal(left, right - 1),
            )

        return internal(0, len(nums) - 1) >= 0
