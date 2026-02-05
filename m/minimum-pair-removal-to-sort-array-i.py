class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        n = len(nums)
        result = 0

        while True:
            if n == 1:
                return result

            is_non_decreasing = True
            minimal_pair_sum = float('inf')
            minimal_pair_sum_index = -1
            for index in range(n - 1, 0, -1):
                if nums[index - 1] > nums[index]:
                    is_non_decreasing = False

                pair_sum = nums[index - 1] + nums[index]
                if pair_sum <= minimal_pair_sum:
                    minimal_pair_sum = pair_sum
                    minimal_pair_sum_index = index

            if is_non_decreasing:
                return result

            result += 1
            nums = nums[:minimal_pair_sum_index - 1] + [minimal_pair_sum] + nums[minimal_pair_sum_index + 1:]
            n -= 1
