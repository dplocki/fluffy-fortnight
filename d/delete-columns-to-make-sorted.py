class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs[0])
        result = [False] * n
        previous = 'a' * n

        for string in strs:
            for i, s in enumerate(string):
                if s < previous[i]:
                    result[i] = True

            previous = string

        return sum(1 for i in result if i)
