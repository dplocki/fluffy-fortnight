MOD = 10**9 + 7


class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        segments = n - 1
        groups = (k << 1) + 1

        @cache
        def internal(group: int, segments_taken: int) -> int:
            remaining = segments - segments_taken
            if group == groups - 2: # last k-segment
                return max(remaining, 0)

            k_segments_left = k - (group >> 1) - 1
            if group & 1 == 1: # is k-segment
                return sum(
                    internal(group + 1, segments_taken + s)
                    for s in range(1, remaining - k_segments_left + 1)
                )

            return sum(
                internal(group + 1, segments_taken + s)
                for s in range(remaining - k_segments_left + 1)
            )

        return internal(0, 0) % MOD
