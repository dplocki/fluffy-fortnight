class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights_len = len(heights)

        def previous(start: int, height: int) -> int:
            result = 0
            for index in range(start - 1, -1, -1):
                if heights[index] < height:
                    return result
  
                result += 1

            return result

        def future(start: int, height) -> int:
            result = 0
            for index in range(start + 1, heights_len):
                if heights[index] < height:
                    return result
  
                result += 1

            return result

        return max(
            height * (1 + previous(index, height) + future(index, height))
            for index, height in enumerate(heights))
