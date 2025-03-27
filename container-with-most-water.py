class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        result = 0
        
        while left < right:
            left_height = height[left]
            right_height = height[right]

            result = max(result, min(left_height, right_height) * (right - left))

            if left_height < right_height:
                left += 1
            else:
                right -= 1

        return result
