class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        result = 0
        prev_assing = -nums[-1]

        for num in nums:
            current_assign = max(min(num + k, prev_assing + 1), num - k)

            if current_assign > prev_assing:
                prev_assing = current_assign
                result += 1

        return result
