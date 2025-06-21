class Solution:
    def isHappy(self, n: int) -> bool:
        was = set()

        while True:
            r = 0
            while n > 0:
                r += (n % 10) ** 2
                n //= 10

            n = r
            if n == 1:
                return True
            if n in was:
                return False
            was.add(n)
