class Solution:
    def smallestNumber(self, n: int) -> int:
        return int(format(n, 'b').replace('0', '1'), 2)
