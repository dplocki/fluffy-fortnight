class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        y_edges = []
        for x, current_y, l in squares:
            y_edges.append((current_y, True, x, x + l))
            y_edges.append((current_y + l, False, x, x + l))

        y_edges.sort()

        blocks = []
        previous_y = y_edges[0][0]
        total_area = 0
        areas = []

        for current_y, is_block_finish, start_x, end_x in y_edges:
            if current_y > previous_y and blocks:
                heigh = current_y - previous_y
                width = self.union_len(blocks)
                areas.append((previous_y, heigh, width))
                total_area += heigh * width

            if is_block_finish:
                blocks.append((start_x, end_x))
            else:
                blocks.remove((start_x, end_x))

            previous_y = current_y

        half_area = total_area / 2
        accumulate_area = 0
        for current_y, heigh, width in areas:
            if accumulate_area + heigh * width >= half_area:
                return current_y + (half_area - accumulate_area) / width
            accumulate_area += heigh * width

    def union_len(self, intervals):
        intervals.sort()
        res = 0
        end = -10**30

        for a, b in intervals:
            if a > end:
                res += b - a
                end = b
            elif b > end:
                res += b - end
                end = b

        return res
