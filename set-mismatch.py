class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        numbers = set()
        correct = set(range(1, n + 1))
        result = None

        for num in nums:
            if num not in numbers:
                numbers.add(num)
                correct.remove(num)
            else:
                result = num

        return [result, correct.pop()]
