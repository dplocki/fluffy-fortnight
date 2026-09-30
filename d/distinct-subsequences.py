class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        s_len, t_len = len(s), len(t)


        @cache
        def internal(s_index: int, t_index: int) -> int:
            if t_index == t_len:
                return 1

            if s_index == s_len:
                return 0

            skip = internal(s_index + 1, t_index)
            not_skip = 0 if s[s_index] != t[t_index] else internal(s_index + 1, t_index + 1)

            return not_skip + skip


        return internal(0, 0)
