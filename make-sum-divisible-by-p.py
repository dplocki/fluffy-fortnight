class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        target_reminder = sum(nums) % p
        if target_reminder == 0:
            return 0

        def internal():
            current = 0
            reminders = {0: -1}
            for index, num in enumerate(nums):
                current = (current + num) % p 

                seek_reminder = (current - target_reminder + p) % p
                if seek_reminder in reminders:
                    length = index - reminders[seek_reminder]
                    if length < len(nums):
                        yield length

                reminders[current] = index

        return min(internal(), default=-1)
