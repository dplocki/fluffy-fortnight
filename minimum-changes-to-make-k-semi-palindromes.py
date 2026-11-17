def segment_cost(s: str, left: int, right: int, factors: list) -> int:
    best = right
    for d in factors[right]:
        groups = right // d
        changes = 0

        for offset in range(d):
            for t in range(groups // 2):
                if (s[left + offset + t * d] == s[left + offset + (groups - 1 - t) * d]):
                    continue

                changes += 1

        best = min(best, changes)

    return best


class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        factors = [[] for _ in range(n + 1)]

        for d in range(1, n // 2 + 1):
            for m in range(d * 2, n + 1, d):
                factors[m].append(d)

        costs = [[0] * n for _ in range(n)]

        for left in range(n - 1):
            for right in range(left + 1, n):
                costs[left][right] = segment_cost(s, left, right - left + 1, factors)

        @cache
        def solve(seg: int, start: int) -> int:
            if seg == 1:
                return costs[start][n - 1]

            limit = n - 1 - 2 * (seg - 1)
            return min(
                costs[start][e] + solve(seg - 1, e + 1)
                for e in range(start + 1, limit + 1)
            )

        return solve(k, 0)
