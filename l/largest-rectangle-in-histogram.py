class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights_len = len(heights)
        left_indexes = [-1] * heights_len
        right_indexes = [heights_len] * heights_len
        stack = []

        for index, height in enumerate(heights):
            while stack and heights[stack[-1]] >= height:
                right_indexes[stack[-1]] = index
                stack.pop()

            if stack:
                left_indexes[index] = stack[-1]

            stack.append(index)

        max_area = 0
        for index, height in enumerate(heights):
            max_area = max(max_area, height * (right_indexes[index] - left_indexes[index] - 1))

        return max_area
