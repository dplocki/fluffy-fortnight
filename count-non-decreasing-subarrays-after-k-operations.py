class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        result = n

        for start in range(n - 1):
            prev = nums[start]
            left = k

            for i in range(start + 1, n):
                need = prev - nums[i]
                if need > 0:
                    if left >= need:
                        left -= need
                    else:
                        break
                
                prev = max(prev, nums[i])
                result += 1

        return result
