class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        target_reminder = sum(nums) % p
        if target_reminder == 0:
            return 0

        nums_len = len(nums)
        current = 0
        reminders = {0: -1}
        result = nums_len

        for index, num in enumerate(nums):
            current = (current + num) % p 

            seek_reminder = (current - target_reminder + p) % p
            if seek_reminder in reminders:
                result = min(result, index - reminders[seek_reminder])

            reminders[current] = index

        return -1 if result == nums_len else result
