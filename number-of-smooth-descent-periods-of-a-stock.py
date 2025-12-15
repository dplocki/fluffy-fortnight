class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        result = 0
        period = 1
        for a, b in zip(prices,  prices[1:]):
            if a - b == 1:
                period += 1
            else:
                result += (period + 1) * period >> 1
                period = 1

        result += (period + 1) * period >> 1
        return result
