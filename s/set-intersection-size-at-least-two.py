class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        result = 0
        last = -1
        prelast = -1

        for start, end in sorted(intervals, key=lambda interval: (interval[1], -interval[0])):
            if start <= prelast:
                continue

            if start > last:
                result += 2
                prelast = end - 1
                last = end
                continue

            result += 1
            prelast = last
            last = end

        return result
