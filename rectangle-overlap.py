class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        x_end = max(rec1[0], rec2[0])
        x_begin = min(rec1[2], rec2[2])
        y_end = max(rec1[1], rec2[1])
        y_begin = min(rec1[3], rec2[3])

        return x_end < x_begin and y_end < y_begin
