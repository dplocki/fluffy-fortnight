class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        max_nums = len(nums)
        nums.sort()

        def interal(start: int, current_subset: List[int]):
            yield tuple(current_subset)

            for index in range(start, max_nums):
                if index != start and nums[index] == nums[index - 1]:
                    continue

                current_subset.append(nums[index])
                yield from interal(index + 1, current_subset)
                current_subset.pop()

        return list(interal(0, []))
