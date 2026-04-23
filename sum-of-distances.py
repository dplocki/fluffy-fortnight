class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        indexes = {}

        for index, num in enumerate(nums):
            if num not in indexes:
                indexes[num] = []

            indexes[num].append(index)

        result = []
        for index, num in enumerate(nums):
            result.append(sum(abs(index - i) for i in indexes[num]))

        return result
