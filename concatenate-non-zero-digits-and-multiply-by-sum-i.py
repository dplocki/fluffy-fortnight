class Solution:
    def sumAndMultiply(self, n: int) -> int:
        digits = list(map(int, str(n)))
        x_str = ''.join(map(str, filter(lambda d: d != 0, digits)))
        if x_str:
            return int(x_str) * sum(digits)
        
        return 0
