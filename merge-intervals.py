class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=itemgetter(0), reverse=True)

        def internal():
            current = intervals.pop()
            while intervals:
                interval = intervals.pop()

                if interval[0] <= current[1]:
                    current = (min(interval[0], current[0]), max(interval[1], current[1]))
                else:
                    yield current
                    current = interval

            yield current

        return list(internal())
