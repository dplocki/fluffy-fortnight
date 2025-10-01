class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        result = numBottles
        empty_bottles = 0

        while numBottles >= numExchange:
            numBottles, empty_bottles = divmod(numBottles, numExchange)
            result += numBottles
            numBottles += empty_bottles

        return result
