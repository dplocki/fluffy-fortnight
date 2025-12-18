class Solution:
    MOD = 10**9 + 7

    def specialTriplets(self, nums: List[int]) -> int:
        lefts = Counter()
        rights = Counter(nums)
        result = 0

        for num in nums:
            rights[num] -= 1
            double_num = num << 1
            result += lefts[double_num] * rights[double_num]
            lefts[num] += 1

        return result % Solution.MOD
