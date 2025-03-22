class Solution:
    def trap(self, heights: List[int]) -> int:
        maxium_height = max(heights)

        return sum(
            w2 - w1 - 1
            for level in range(maxium_height, 0, -1)
            for w1, w2 in pairwise(i for i, w in enumerate(heights) if w >= level)
        )
