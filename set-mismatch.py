class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        numbers, correct = set(), set(range(1, n + 1))
        result = None

        for num in nums:
            if num in numbers:
                result = num
            else:
                numbers.add(num)
                correct.remove(num)

        return [result, correct.pop()]
