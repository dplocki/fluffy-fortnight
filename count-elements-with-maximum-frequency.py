class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        counter = Counter(nums)
        maximum = max(counter.values())

        return sum(
            how_many
            for element, how_many in counter.items()
            if how_many == maximum)
