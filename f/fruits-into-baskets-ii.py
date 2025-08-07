class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        result = 0

        for fruit in fruits:
            index = next((i for i, b in enumerate(baskets) if b >= fruit), None)
            if index == None:
                result += 1
            else:
                baskets[index] = 0

        return result
