class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        return list(map(
            lambda n: n == 0,
            accumulate(nums, lambda number, digit: (number << 1 | digit) % 5)
        ))
