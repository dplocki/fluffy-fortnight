class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = set(nums)
        result = 0

        for number in numbers:
            if number - 1 not in numbers:
                continue

            current_number = number + 1
            while current_number in numbers:
                current_number += 1

            result = max(result, current_number - number + 1)

        return result
