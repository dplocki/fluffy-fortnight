class Solution:
    def largestGoodInteger(self, num: str) -> str:
        digits = list(sorted(self.find_triples(num), reverse=True))

        if not digits:
            return ""

        return digits[0] * 3
        
    def find_triples(self, num: str):
        count = 0
        digit = None
        
        for n in num:
            if n == digit:
                count += 1
            else:
                count = 1

            digit = n

            if count == 3:
                yield digit
