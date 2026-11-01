class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        maximum, minimum = max(s), min(s)

        if all(a <= b for a, b in pairwise(s)):
            return 0

        if n == 2:
            return -1

        if s[0] == minimum or s[-1] == maximum:
            return 1

        for index in range(1, n - 1):
            if s[index] != minimum and s[index] != maximum:
                continue

            return 2

        return 3
