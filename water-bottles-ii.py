class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        empty_bottles = numBottles
        result = numBottles
        full_bottles = 0

        while full_bottles > 0 or empty_bottles >= numExchange:
            if full_bottles > 0:
                result += full_bottles
                empty_bottles += full_bottles
                full_bottles = 0
            
            if empty_bottles >= numExchange:
                full_bottles += 1
                empty_bottles -= numExchange
                numExchange += 1

        return result
