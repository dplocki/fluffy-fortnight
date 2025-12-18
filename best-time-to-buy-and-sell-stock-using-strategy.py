class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        n = len(prices)
        s = defaultdict(int)
        t = defaultdict(int)

        for index, (a, b) in enumerate(zip(prices, strategy), 1):
            s[index] = s[index - 1] + a * b
            t[index] = t[index - 1] + a

        return max(s[n], max(
            s[n] - (s[index] - s[index - k]) + t[index] - t[index - k // 2]
            for index in range(k, n + 1)))
