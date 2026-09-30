class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        is_palindrome = [[False] * n for _ in range(n)]

        for length in range(1, n + 1):
            for left in range(n - length + 1):
                right = left + length - 1
                is_palindrome[left][right] = s[left] == s[right] and (length <= 2 or is_palindrome[left + 1][right - 1])

        dp = defaultdict(int)
        for right in range(n):
            dp[right + 1] = dp[right]

            for left in range(right - k + 2):
                if not is_palindrome[left][right]:
                    continue
                
                dp[right + 1] = max(dp[right + 1], dp[left] + 1)

        return dp[n]
