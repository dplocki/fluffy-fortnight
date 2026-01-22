class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        n = len(nums)
        result = 0

        while True:
            if n == 1:
                return result

            is_non_decreasing = True
            minimal_pair_sum = float('inf')
            cache = {}
            for index in range(n - 1, 0, -1):
                if nums[index - 1] > nums[index]:
                    is_non_decreasing = False
                pair_sum = nums[index - 1] + nums[index]
                minimal_pair_sum = min(minimal_pair_sum, pair_sum)
                cache[pair_sum] = index

            if is_non_decreasing:
                return result

            result += 1
            index = cache[minimal_pair_sum]
            nums = nums[:index - 1] + [minimal_pair_sum] + nums[index + 1:]
            n -= 1
