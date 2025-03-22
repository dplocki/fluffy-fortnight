class Solution:
    def trap(self, heights: List[int]) -> int:
        return sum(
            (min(left_height, right_height) - height)
            for left_height, right_height, height in (
                (
                    max(heights[:index + 1]),
                    max(heights[index:]),
                    height
                )
                for index, height in enumerate(heights)
            )
        )
