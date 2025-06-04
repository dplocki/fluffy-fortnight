class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        current = []
        max_nums = len(nums)

        def internal(start_index):
            if len(current) == 4 and sum(current) == target:
                yield tuple(current)
                return

            for index in range(start_index, max_nums):
                if index > start_index and nums[index] == nums[index - 1]:
                    continue

                current.append(nums[index])
                yield from internal(index + 1)
                current.pop()

        nums.sort()
        return list(internal(0))
