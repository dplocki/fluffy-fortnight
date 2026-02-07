class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        numbers = set(range(1, n + 1))
        for num in nums:
            if num in numbers:
                numbers.remove(num)
        
        return list(numbers)
