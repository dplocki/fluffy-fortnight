class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)

        lefts = [1] * n
        rights = [1] * n

        for index in range(1, n):
            if ratings[index] > ratings[index - 1]:
                lefts[index] = lefts[index - 1] + 1

        for index in range(n - 2, -1, -1):
            if ratings[index] > ratings[index + 1]:
                rights[index] = rights[index + 1] + 1

        return sum(max(l, r) for l, r in zip(lefts, rights))
