class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        counter = defaultdict(int)
        max_difference = 0

        for a, b in zip(nums1, nums2):
            difference = abs(a - b)
            counter[difference] += 1
            max_difference = max(max_difference, difference)

        operations = k1 + k2 
        while max_difference > 0 and operations > 0:
            change = min(operations, counter[max_difference])
            operations -= change
            counter[max_difference] -= change
            counter[max_difference - 1] += change
            max_difference -= 1

        return sum(v * k * k for k, v in counter.items())
