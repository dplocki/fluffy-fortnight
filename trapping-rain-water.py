class Solution:
    def trap(self, heights: List[int]) -> int:
        if not heights:
            return 0
        
        water = 0
        left, right = 0, len(heights) - 1
        max_left, max_right = heights[left], heights[right]
        
        while left <= right:
            max_left = max(max_left, heights[left])
            max_right = max(max_right, heights[right])
            
            if max_left < max_right:
                water += max_left - heights[left]
                left += 1
            else:
                water += max_right - heights[right]
                right -= 1
        
        return water
