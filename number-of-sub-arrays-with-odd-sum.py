MOD = (10 ** 9) + 7


class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        n = len(arr)
        count = 0
        dp = [[0, 0], [0, 0]]

        for index in range(n):
            current = index & 1
            parity = arr[index] & 1
            dp[parity][current] = (1 + dp[0][1 - current]) % MOD
            dp[1 - parity][current] = dp[1][1 - current] % MOD

            count = (count + dp[1][current]) % MOD

        return count
