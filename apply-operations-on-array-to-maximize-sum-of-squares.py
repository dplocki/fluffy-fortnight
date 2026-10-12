MOD = 10**9 + 7

class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        bit_count = [0] * 30

        for num in nums:
            for i in range(30):
                if num & (1 << i):
                    bit_count[i] += 1

        result = 0
        for _ in range(k):
            current = 0
            for j in range(29, -1, -1):
                if bit_count[j] > 0:
                    current |= 1 << j
                    bit_count[j] -= 1

            result = (result + current * current) % MOD

        return result

