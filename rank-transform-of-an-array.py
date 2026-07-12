class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        ranks = {}
        rank = 1

        for number in sorted(arr):
            if number in ranks:
                continue

            ranks[number] = rank
            rank += 1

        return list(
            ranks[number]
            for number in arr
        )
