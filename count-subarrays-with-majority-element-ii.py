class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        pre = [0] * (n * 2 + 1)
        pre[n] = 1
        cnt = n
        result = presum = 0

        for num in nums:
            if num == target:
                presum += pre[cnt]
                cnt += 1
                pre[cnt] += 1
            else:
                cnt -= 1
                presum -= pre[cnt]
                pre[cnt] += 1

            result += presum

        return result
