class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        maximum = max(nums)

        frequencies = [0] * (maximum + 1)
        for num in nums:
            frequencies[num] += 1

        for i in range(1, maximum + 1):
            for j in range(i * 2, maximum + 1, i):
                frequencies[i] += frequencies[j]

        for i in range(1, maximum + 1):
            frequencies[i] = frequencies[i] * (frequencies[i] - 1) // 2

        for i in range(maximum, 0, -1):
            for j in range(i * 2, maximum + 1, i):
                frequencies[i] -= frequencies[j]

        for i in range(1, maximum + 1):
            frequencies[i] += frequencies[i - 1]

        return [
            bisect_left(frequencies, q + 1)
            for q in queries
        ]
