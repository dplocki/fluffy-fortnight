class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        maximum = nums[0]
        prefixGcd = []
        n = 0

        for num in nums:
            maximum = max(maximum, num)
            prefixGcd.append(math.gcd(maximum, num))
            n += 1

        prefixGcd.sort()

        return sum(
            math.gcd(prefixGcd[i], prefixGcd[-(i + 1)])
            for i in range(n >> 1)
        )
