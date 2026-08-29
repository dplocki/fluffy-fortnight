def get_digits(n: int) -> Generator[int, None, None]:
    while n:
        yield n % 10
        n //= 10

class Solution:
    def checkDivisibility(self, n: int) -> bool:
        digits = list(get_digits(n))
        return n % (sum(digits) + reduce(operator.mul, digits)) == 0
