class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()
        expected = nums[0]
        result = []

        for num in nums:
            while expected != num:
                result.append(expected)
                expected += 1
            expected += 1

        return result
