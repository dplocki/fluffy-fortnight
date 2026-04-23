class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        indexes = {}

        for index, num in enumerate(nums):
            if num not in indexes:
                indexes[num] = []

            indexes[num].append(index)

        return [
            sum(abs(index - i) for i in indexes[num])
            for index, num in enumerate(nums)
        ]
