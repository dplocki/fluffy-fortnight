class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums_size = len(nums)
        nums.sort()

        def internal(current: List[int]=[], used: List[bool]=[False] * nums_size):
            if len(current) == nums_size:
                yield tuple(current)
                return

            for index in range(nums_size):
                if used[index] or (index > 0 and nums[index] == nums[index - 1] and not used[index - 1]):
                    continue

                used[index] = True
                current.append(nums[index])

                yield from internal(current)

                current.pop()
                used[index] = False

        return list(internal())
