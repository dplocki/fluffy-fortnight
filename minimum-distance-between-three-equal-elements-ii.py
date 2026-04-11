class Solution:
    def minimumDistance(self, nums: List[int]) -> int:

        def internal():
            n = len(nums)
            values = {}

            for index, num in enumerate(nums):
                if num not in values:
                    values[num] = []
                
                indexes = values[num]
                if len(indexes) > 1:
                    yield (index - indexes[-2]) << 1

                indexes.append(index)

        return min(internal(), default=-1)
