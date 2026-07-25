class Solution:
    def maxProduct(self, n: int) -> int:
        sorted_digits = sorted(map(int, str(n)))[-2:]
        return sorted_digits[-1] * sorted_digits[-2]
