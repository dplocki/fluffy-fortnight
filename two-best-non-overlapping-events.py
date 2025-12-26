class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort()

        return max(
            chain.from_iterable([
                (a_v + b_v
                for (a_s, a_f, a_v), (b_s, b_f, b_v) in combinations(events, 2)
                if b_s > a_f),
                map(itemgetter(2), events)]))
