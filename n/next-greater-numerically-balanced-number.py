class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        for number in count(n + 1):
            digits = [0] * 10

            n = number
            while n > 0:
                n, d = divmod(n, 10)
                digits[d] += 1

            if all(count == 0 or count == d for d, count in enumerate(digits)):
                return number
