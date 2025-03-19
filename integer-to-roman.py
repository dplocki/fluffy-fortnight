ROMANS = 'IVXLCDM'

class Solution:

    def intToRoman(self, num: int) -> str:
        return ''.join(self.intToRomanTokens(num))[::-1]

    def intToRomanTokens(self, num):
        index = 0
        while index < len(ROMANS) - 2:
            digit = num % 10
            if digit == 4:
                yield ROMANS[index + 1]
                yield ROMANS[index]
            elif digit == 9:
                yield ROMANS[index + 2]
                yield ROMANS[index]
            elif digit >= 5:
                for i in range(digit - 5):
                    yield ROMANS[index]

                if digit >= 5:
                    yield ROMANS[index + 1]
            else:
                for i in range(digit):
                    yield ROMANS[index]

            index += 2
            num //= 10

        for i in range(num):
            yield 'M'
