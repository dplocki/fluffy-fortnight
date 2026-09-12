class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        order = sorted(range(n), key=lambda i: intervals[i][1])
        rights = [intervals[i][1] for i in order]

        previous = [(0, [])] * (n + 1)
        for _ in range(4):
            current = [(0, [])] * (n + 1)
            for p in range(1, n + 1):
                interval = order[p - 1]
                left, _, weight = intervals[interval]
                previous_index = bisect_left(rights, left)
                score, result = previous[previous_index]
                current[p] = min((score - weight, sorted(result + [interval])), current[p - 1])

            previous = current

        return previous[n][1]
