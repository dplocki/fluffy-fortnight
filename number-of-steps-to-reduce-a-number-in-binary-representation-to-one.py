class Solution:
    def numSteps(self, s: str) -> int:
        number = int(s, 2)
        result = 0

        while number != 1:
            if number % 2 == 0:
                number >>= 1
            else:
                number += 1
            result += 1

        return result
