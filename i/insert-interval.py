class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key=itemgetter(0), reverse=True)

        def internal():
            current = intervals.pop()
            while intervals:
                interval = intervals.pop()

                if interval[0] <= current[1]:
                    current = (current[0], max(interval[1], current[1]))
                else:
                    yield current
                    current = interval

            yield current

        return list(internal())
