class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        return sum(map(lambda n: 1 if n != 0 else 0, map(lambda n: n % 3, nums)))
