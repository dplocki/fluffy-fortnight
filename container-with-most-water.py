class Solution:
    def maxArea(self, height: List[int]) -> int:
        return max(
            min(height[left], height[right]) * (right - left)
            for left, right in combinations(range(len(height)), 2)
        )
