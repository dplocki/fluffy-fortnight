class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        n = len(nums)

        phase1 = phase2 = phase3 = result = -inf
        for i in range(1, n):
            first, second = nums[i - 1], nums[i]

            current_phase1 = current_phase2 = current_phase3 = -inf
            if first < second:
                current_phase1 = max(first + second, phase1 + second)
                current_phase3 = max(phase3 + second, phase2 + second)
            elif first > second:
                current_phase2 = max(phase2 + second, phase1 + second)

            result = max(result, current_phase3)
            phase1, phase2, phase3 = current_phase1, current_phase2, current_phase3

        return result
