class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        last_nums_index = len(nums) - 1
        
        result = None
        result_differnce = 10**5

        for index in range(last_nums_index - 1):
            left, right = index + 1, last_nums_index

            while left < right:
                current = nums[left] + nums[right] + nums[index]

                if result_differnce > abs(target - current):
                    result = current
                    result_differnce = abs(target - current)
                
                if current < target:
                    left += 1
                elif current > target:
                    right -= 1
                else:
                    return current
                
        return result
