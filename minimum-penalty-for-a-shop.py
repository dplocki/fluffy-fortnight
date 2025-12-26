class Solution:
    def bestClosingTime(self, customers: str) -> int:
        return min(enumerate(
                accumulate(customers, lambda p, c: p - 1 if c == 'Y' else p + 1, initial=0)
            ),
            key=itemgetter(1)
        )[0]
