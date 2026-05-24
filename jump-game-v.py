class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n, dp = len(arr), {}
        
        def internal(start: int) -> int:
            if start < 0 or start >= n:
                return 0

            if start in dp:
                return dp[start]

            result = 0
            for index in range(d):
                if start - index - 1 < 0:
                    break

                if arr[start] <= arr[start - index - 1]:
                    break

                result = max(result, internal(start - index - 1))

            for index in range(d):
                if start + index + 1 >= n:
                    break

                if arr[start] <= arr[start + index + 1]:
                    break

                result = max(result, internal(start + index + 1))

            dp[start] = result + 1
            return result + 1

        return max(internal(i) for i in range(len(arr)))
