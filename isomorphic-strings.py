class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_last_seen, t_last_seen = {}, {}

        for index, (sch, tch) in enumerate(zip(s, t)):
            if s_last_seen.get(sch, None) != t_last_seen.get(tch, None):
                return False

            s_last_seen[sch] = t_last_seen[tch] = index

        return True
