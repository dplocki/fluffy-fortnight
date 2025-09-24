class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        counter = Counter(nums)
        counter_values = counter.values()
        maximum = max(counter_values)

        return sum(
            how_many
            for how_many in counter_values
            if how_many == maximum)
