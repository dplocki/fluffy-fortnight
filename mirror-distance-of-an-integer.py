class Solution:
    def mirrorDistance(self, n: int) -> int:
        return abs(n - self.reverse_number(n))
    
    def reverse_number(self, num: int) -> int:
        result = 0

        while num:
            digit = num % 10

            result *= 10
            result += digit

            num //= 10
    
        return result
