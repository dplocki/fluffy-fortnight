class Solution:
    def minOperations(self, nums: List[int]) -> int:
        stack = [0]
        result = 0

        for num in nums:
            while num < stack[-1]:
                stack.pop()

            if num == 0:
                continue

            if num > stack[-1]:
                result += 1

            stack.append(num)

        return result
