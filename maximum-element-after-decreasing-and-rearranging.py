class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        result = 1

        for num in arr:
            if num >= result:
                result += 1

        return result - 1
