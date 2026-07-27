MOD = 10**9 + 7

class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        m = max(nums)
        dp = { (0, 0): 1 }

        for num in nums:
            ndp = {}

            for j in range(m + 1):
                divisor1 = math.gcd(j, num)

                for k in range(m + 1):
                    value = dp.get((j, k), 0)
                    if value == 0:
                        continue

                    divisor2 = math.gcd(k, num)
                    ndp[j, k] = (ndp.get((j, k), 0) + value) % MOD

                    ndp[divisor1, k] = (ndp.get((divisor1, k), 0) + value) % MOD
                    ndp[j, divisor2] = (ndp.get((j, divisor2), 0) + value) % MOD

            dp = ndp

        result = 0
        for j in range(1, m + 1):
            result = (result + dp.get((j, j), 0)) % MOD

        return result
