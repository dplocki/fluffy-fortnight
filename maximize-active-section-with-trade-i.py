class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        index, n = 0, len(s)
        best_group = 0
        previous = -inf

        while index < n:
            start = index

            while index < n and s[index] == s[start]:
                index += 1

            if s[start] == '0':
                curent = index - start
                best_group = max(best_group, previous + curent)
                previous = curent

        return s.count('1') + best_group
