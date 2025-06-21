class Solution:
    MIN = -2**31
    MAX = 2**31 - 1

    def divide(self, dividend: int, divisor: int) -> int:
        result = 0
        negative = (dividend < 0) != (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)

        while dividend >= divisor:
            temp = divisor
            multiple = 1
            while dividend >= (temp << 1):
                temp <<= 1
                multiple <<= 1
            dividend -= temp
            result += multiple

        result = -result if negative else result

        if result > Solution.MAX:
            result = Solution.MAX
        elif result < Solution.MIN:
            result = Solution.MIN
        
        return result
