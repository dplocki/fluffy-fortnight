class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        return list(map(
            lambda n: n % 5 == 0,
            accumulate(nums, lambda number, digit: number * 2 + digit)
        ))
