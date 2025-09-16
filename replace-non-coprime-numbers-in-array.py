from math import gcd

class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        stack = []

        for num in nums:
            stack.append(num)

            while len(stack) > 1:
                a, b = stack[-2:]
                common_divisor = gcd(a, b)
                if common_divisor == 1:
                    break

                stack.pop()
                stack[-1] = a * b // common_divisor

        return stack
