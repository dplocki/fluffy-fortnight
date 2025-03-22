class Solution:
    def trap(self, heights: List[int]) -> int:
        heights_length = len(heights)

        return sum(
            max(min(left_height, right_height) - hight, 0)
            for left_height, right_height, hight in (
                (
                    max(heights[:index]) if index > 0 else 0,
                    max(heights[index:]) if index < heights_length else 0,
                    heights[index]
                )
                for index in range(heights_length)
            )
        )
