class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = []

        while columnNumber:
            columnNumber -= 1
            result.append(ascii_uppercase[(columnNumber) % 26])
            columnNumber //= 26

        return ''.join(result[::-1])
