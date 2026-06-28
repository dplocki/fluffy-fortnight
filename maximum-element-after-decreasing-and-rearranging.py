class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        result = 0

        for index, num in enumerate(arr):
            result = min(result + 1, index + 1, num)
        
        return result
