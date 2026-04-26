class Solution:
    def minimumDistance(self, nums: List[int]) -> int:

        def internal():
            n = len(nums)
            for i in range(n - 2):
                for j in range(i + 1, n - 1):
                    if nums[i] != nums[j]:
                        continue

                    for k in range(j + 1, n):
                        if nums[j] != nums[k]:
                            continue

                        yield abs(i - j) + abs(j - k) + abs(k - i)

        return min(internal(), default=-1)
