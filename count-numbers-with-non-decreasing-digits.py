class Solution:
    def countNumbers(self, l: str, r: str, b: int) -> int:
        return sum(1
            for number in range(int(l), int(r) + 1)
            if self.check_digits(number, b))

    def check_digits(self, value, b):
        last_digit = b + 1

        while value:
            digit = value % b
            if digit > last_digit:
                return False
 
            last_digit = digit
            value //= b

        return True
