class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        return (min(self.find_the_longest_consetive(hBars), self.find_the_longest_consetive(vBars))
                + 1) ** 2
    
    def find_the_longest_consetive(self, bars: List[int]) -> int:
        result, current_length = 1, 1

        for previous, current in pairwise(sorted(bars)):
            if previous + 1 == current:
                current_length += 1
            else:
                result = max(result, current_length)
                current_length = 1
       
        return max(result, current_length)
