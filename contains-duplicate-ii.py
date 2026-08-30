class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        duplicates = {}

        for index, num in enumerate(nums):
            if num in duplicates:
                if index - duplicates[num] <= k:
                    return True

            duplicates[num] = index

        return False
