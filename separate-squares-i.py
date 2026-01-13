class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        half_area = sum((l**2 for _, _, l in squares)) / 2
        events = []
        for _, y, l in squares:
            events.append((y, l))
            events.append((y + l, -l))
        events.sort()

        area, width, prev_y = 0, 0, 0
        for y, l in events:
            new_area = width * (y - prev_y)
            if area + new_area >= half_area:
                return prev_y + (half_area - area) / width
    
            area += new_area
            width += l
            prev_y = y
