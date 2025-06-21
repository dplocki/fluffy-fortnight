class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        previous = None
        for character in s:
            if character == 'M':
                if previous == 'C':
                    result -= 200
                result += 1000
            elif character == 'D':
                if previous == 'C':
                    result -= 200
                result += 500
            elif character == 'C':
                if previous == 'X':
                    result -= 20
                result += 100
            elif character == 'L':
                if previous == 'X':
                    result -= 20
                result += 50
            elif character == 'X':
                if previous == 'I':
                    result -= 2
                result += 10
            elif character == 'V':
                if previous == 'I':
                    result -= 2
                result += 5
            elif character == 'I':
                result += 1

            previous = character

        return result
