class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        result = 0
        used = set()

        for f in fruits:
            index = next((i for i, b in enumerate(baskets) if i not in used and b >= f), None)
            if index == None:
                result += 1
            else:
                used.add(index)

        return result
