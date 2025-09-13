class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        result = 0
        simple_nums = list(self.simplified(nums))

        for a, b, c in zip(simple_nums, simple_nums[1:], simple_nums[2:]):
            if a > b < c or a < b > c:
                result += 1

        return result

    def simplified(self, nums):
        prev = None
        for n in nums:
            if n != prev:
                yield n
                
            prev = n
