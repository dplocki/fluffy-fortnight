class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(self.internal, nums, (0, 0))[1]

    def internal(self, previous: Tuple[int, int], num: int):
        just_one, just_twice = previous

        return (
            (~just_one & just_twice & num) | (just_one & ~just_twice & ~num),
            ~just_one & (just_twice ^ num)
        )
