class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        numbers = [i + 1 for i in range(n)]
        return list(combinations(numbers, k))
