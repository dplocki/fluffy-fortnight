class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        result = 0
        period = 1
        for a, b in zip_longest(prices,  prices[1:], fillvalue=-1):
            if a - b == 1:
                period += 1
                continue

            result += (period + 1) * period >> 1
            period = 1

        return result
