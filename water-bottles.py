class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        result = numBottles
        empty_bottles = 0

        while numBottles + empty_bottles >= numExchange:
            numBottles, empty_bottles = divmod(numBottles + empty_bottles, numExchange)
            result += numBottles

        return result
