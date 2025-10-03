class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        empty_bottles = numBottles
        result = numBottles

        while empty_bottles >= numExchange:
            result += 1
            empty_bottles -= numExchange - 1
            numExchange += 1

        return result
