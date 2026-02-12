class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        smaller_counts = {}
        for index, value in enumerate(sorted(nums)):
            if value not in smaller_counts:
                smaller_counts[value] = index

        return [ 
            smaller_counts[num]
            for num in nums
        ]
