class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        heights = [0] * len(matrix[0])
        result = 0
        for row in matrix:
            for index, c in enumerate(row):
                if c == '1':
                    heights[index] += 1
                else:
                    heights[index] = 0

            result = max(result, self.largestRectangleArea(heights))

        return result

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

        return max(
            height * (right_indexes[index] - left_indexes[index] - 1)
            for index, height in enumerate(heights)
        )
