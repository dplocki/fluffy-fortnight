class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        return target[0] + sum(
            max(0, current_height - previous_height)
            for previous_height, current_height in pairwise(target)
        )
