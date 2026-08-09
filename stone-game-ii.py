class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)

        suffix_sum = [0] * n
        suffix_sum[-1] = piles[-1]
        for index in range(n - 2, -1, -1):
            suffix_sum[index] = piles[index] + suffix_sum[index + 1]
        
        @cache
        def internal(start: int, m: int) -> int:
            if start + 2 * m >= n:
                return suffix_sum[start]
                
            return suffix_sum[start] - min(
                internal(start + x, max(m, x))
                for x in range(1, 2 * m + 1)
            )

        return internal(0, 1)
