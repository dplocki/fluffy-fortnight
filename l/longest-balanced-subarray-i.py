class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)
        result = 0

        for a in range(n):
            counts = [0, 0]
            vis = set()
            for b in range(a, n):
                if nums[b] not in vis:
                    counts[nums[b] & 1] += 1
                    vis.add(nums[b])

                if counts[0] == counts[1]:
                    result = max(result, b - a + 1)

        return result
