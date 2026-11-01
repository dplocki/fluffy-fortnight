MOD = 10 ** 9 + 7

class Solution:
    def numOfWays(self, nums: list[int]) -> int:

        def dfs(nums: list[int]) -> int:
            n = len(nums)
            if n < 3: 
                return 1

            lefts, rights = [], []

            for num in nums:
                if num < nums[0]:
                    lefts.append(num)
                elif num > nums[0]:
                    rights.append(num)

            return dfs(lefts) * dfs(rights) * comb(n - 1, len(lefts)) % MOD


        return (dfs(nums) - 1) % MOD
