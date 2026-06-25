class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        result = 0
        n = len(nums)

        for start in range(n):
            length = 0
            target_count = 0

            for end in range(start, n):
                length += 1
                if nums[end] == target:
                    target_count += 1

                if target_count > (length >> 1):
                    result += 1

        return result
