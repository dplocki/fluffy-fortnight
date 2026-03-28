class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)

        for left, left_value in enumerate(numbers):
            for right in range(left + 1, n):
                current_sum = left_value + numbers[right]
                if current_sum == target:
                    return (left + 1, right + 1)
                elif current_sum > target:
                    break
