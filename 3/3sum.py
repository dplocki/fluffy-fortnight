class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        return list(set(self.interal(nums)))

    def interal(self, nums: List[int]):
        max_length = len(nums) - 1
        nums.sort()

        for index, current_value in enumerate(nums):
            if index > 0 and current_value == nums[index - 1]:
                continue

            left = index + 1
            right = max_length

            while left < right:
                total = current_value + nums[left] + nums[right]

                if total > 0:
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    yield current_value, nums[left], nums[right]
                    right -= 1
                    left += 1


