class Solution:
    def rotatedDigits(self, n: int) -> int:
        return sum(1
            for i in range(1, n + 1)
            if self.is_number_good(i)
        )


    def is_number_good(self, n: int):
        it_stays_the_same = True

        for digit in self.to_digits(n):
            if digit == 3 or digit == 4 or digit == 7:
                return False

            if digit == 2 or digit == 5 or digit == 6 or digit == 9:
                it_stays_the_same = False

        return not it_stays_the_same


    def to_digits(self, n: int):
        while n:
            yield n % 10
            n //= 10
