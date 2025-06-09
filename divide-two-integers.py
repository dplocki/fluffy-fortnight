class Solution:
    MIN = -2**31
    MAX = 2**31 - 1

    def divide(self, dividend: int, divisor: int) -> int:
        result = 0
        dividend_sign = 1 if dividend > 0 else -1
        divisor_sign = 1 if divisor > 0 else -1
        dividend = abs(dividend)
        divisor = abs(divisor)

        if divisor > 1:
            while True:
                dividend -= divisor
                if dividend >= 0:
                    result += 1
                else:
                    break
        else:
            result = dividend

        if dividend_sign != divisor_sign:
            result = -result

        if result > Solution.MAX:
            result = Solution.MAX
        elif result < Solution.MIN:
            result = Solution.MIN
        
        return result
