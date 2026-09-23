class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        target_sum = sum(nums) - x
        if target_sum < 0:
            return -1 

        current_sum, start = 0, 0 
        best_size = -1

        for end, num in enumerate(nums):
            current_sum += num

            while current_sum > target_sum:
                current_sum -= nums[start]
                start += 1
            
            if current_sum == target_sum:
                best_size = max(best_size, end - start + 1)

        return -1 if best_size < 0 else len(nums) - best_size
