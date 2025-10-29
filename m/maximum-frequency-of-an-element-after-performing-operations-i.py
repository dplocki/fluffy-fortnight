class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        frequency_count = defaultdict(int)
        range_contributions = defaultdict(int)

        for num in nums:
            frequency_count[num] += 1
            range_contributions[num] += 0
            range_contributions[num - k] += 1
            range_contributions[num + k + 1] -= 1

        current_sum = 0
        result = 0

        for position, contribution_delta in sorted(range_contributions.items()):
            current_sum += contribution_delta
            result = max(
                result, 
                min(current_sum, frequency_count[position] + numOperations)
            )

        return result
