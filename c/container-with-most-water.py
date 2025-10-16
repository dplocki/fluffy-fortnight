class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        result = 0

        while left < right:
            in_between = right - left

            if height[left] > height[right]:
                result = max(result, in_between * height[right])
                right -= 1
            else:
                result = max(result, in_between * height[left])
                left += 1
                
        return result
