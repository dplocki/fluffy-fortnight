class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        result = self.internal(dividend, divisor)
        if result > (2**31 - 1):
            return 2**31 - 1
        if result < -2**31:
            return -2**31

        return result

    def internal(self, dividend: int, divisor: int):
        result = 0
        current = 0
        is_negative = False

        if divisor < 0:
            divisor = -divisor
            is_negative = True

        if dividend < 0:
            dividend = -dividend
            is_negative = not is_negative

        if divisor == 1:
            if is_negative:
                return -dividend
            else:
                return dividend

        while True:
            current += divisor
            if current > dividend:
                return result

            if is_negative:
                result -= 1
            else:
                result += 1
