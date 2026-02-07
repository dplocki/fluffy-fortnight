class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        numbers = set(nums)
        result = []
        for number in range(1, n + 1):
            if number not in numbers:
                result.append(number)
        
        return result
