class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        nums, n = set(nums), len(nums)

        for i in range(2 ** n):
            i_str = f"{i:0{n}b}"
            if i_str not in nums:
                return i_str
