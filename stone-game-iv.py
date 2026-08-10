squares = [i ** 2 for i in range(1, isqrt(100_000))]

class Solution:
    @cache
    def winnerSquareGame(self, n: int) -> bool:
        if n == 0:
            return False

        if n in squares:
            return True

        for square in squares:
            if square > n:
                break

            if not self.winnerSquareGame(n - square):
                return True
        
        return False
