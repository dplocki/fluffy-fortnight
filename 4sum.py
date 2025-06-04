class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        current = []
        nums.sort()

        def internal(k, start_index, target):
            if k == 2:
                left, right = start_index, len(nums) - 1
                while left < right:
                    if nums[left] + nums[right] < target:
                        left += 1
                    elif nums[left] + nums[right] > target:
                        right -= 1
                    else:
                        yield (*current, nums[left], nums[right])
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                return

            for index in range(start_index, len(nums) - k + 1):
                if index > start_index and nums[index] == nums[index - 1]:
                    continue

                current.append(nums[index])
                yield from internal(k - 1, index + 1, target - nums[index])
                current.pop()

        return list(internal(4, 0, target))
        
