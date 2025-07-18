class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        results = { (i, n): 0
            for i in range(k)
            for n in range(k)}

        for num in nums:
            current = num % k
            for n in range(k):
                results[n, current] = results[current, n] + 1

        return max(results.values())
