class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        return sum(self.is_symmetric(n) for n in range(low, high + 1))

    def is_symmetric(self, number: int) -> int:
        digits = tuple(self.digits(number))
        digits_count = len(digits)
        if digits_count & 1:
            return False

        middle = digits_count // 2

        return sum(digits[middle:]) == sum(digits[:middle])

    def digits(self, number):
        while number:
            yield number % 10
            number //= 10
