MOD = 10**7 + 9
PRIME = 12541

class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)

        h = [0] * (n + 1)
        p = [0] * (n + 1)
        p[0] = 1
        for i in range(n):
            h[i + 1] = (h[i] * PRIME + nums[i]) % MOD
            p[i + 1] = p[i] * PRIME % MOD

        def check(length):
            frequency = {}
            for l in range(n - length + 1):
                r = l + length
                key = (h[r] - h[l] * p[length] % MOD + MOD) % MOD
                frequency[key] = frequency.get(key, 0) + 1

            return any(times == 1 for times in frequency.values())


        left, right = 1, n
        while left < right:
            middle = left + ((right - left) >> 1)
            if check(middle):
                right = middle
            else:
                left = middle + 1

        return left
