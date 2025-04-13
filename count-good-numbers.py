class Solution:
    def countGoodNumbers(self, n: int) -> int:
        total = 1

        for index in range(n):
            if index % 2 == 0:
                total *= 5
            else:
                total *= 4
        
        return total % (10**9 + 7)
