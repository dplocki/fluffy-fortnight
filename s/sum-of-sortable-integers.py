class Solution:
    def sortableIntegers(self, nums: List[int]) -> int:
        n = len(nums)

        factories = []
        for x in range(1, isqrt(n) + 1):
            if n % x != 0:
                continue

            factories.append(x)
            if n // x == x:
                continue

            factories.append(n // x)

        target = sorted(nums)


        def check(left: List[int], right: List[int]) -> bool:
            L = len(left)

            for i in range(L - 1):
                if left[i] <= left[i + 1]:
                    continue

                return left[i + 1:] + left[:i + 1] == right

            return left == right


        result = 0
        for d in factories:
            for left in range(0, n, d):
                right = left + d - 1

                if not check(nums[left:right + 1], target[left:right + 1]):
                    break
            else:
                result += d

        return result
