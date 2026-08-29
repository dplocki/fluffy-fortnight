def digits(n: str) -> Generator[int, None, None]:
        while n:
            yield n % 10
            n //= 10

class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            if reduce(operator.mul, digits(n), 1) % t == 0:
                return n
            n += 1
