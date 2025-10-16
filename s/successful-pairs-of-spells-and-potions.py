class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        potions_len = len(potions)

        return [
            potions_len - bisect.bisect_left(potions, success / spell)
            for spell in spells
        ]
