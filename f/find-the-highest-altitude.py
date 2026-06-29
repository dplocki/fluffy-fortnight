class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        return max(chain((0, ), accumulate(gain)))
