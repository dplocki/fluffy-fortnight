class Solution:
    def maxProduct(self, n: int) -> int:
        return operator.mul(*sorted(map(int, str(n)))[-2:])
