class Solution:
    def __init__(self):
        self.digits = {str(d):d for d in range(10)}

    def multiply(self, num1: str, num2: str) -> str:
        return str(self.str2int(num1) * self.str2int(num2))

    def str2int(self, num: str) -> int:
        multiplayer = 10 ** (len(num) - 1)
        result = 0

        for d in num:
            result += multiplayer * self.digits[d]
            multiplayer //= 10

        return result
