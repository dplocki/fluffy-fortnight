class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
                
        @cache
        def internal(left: int, right: int) -> int:
            if left == right:
                return piles[left]

            return max(
                piles[left] - internal(left + 1, right),
                piles[right] - internal(left, right - 1),
            )

        return internal(0, len(piles) - 1) > 0
