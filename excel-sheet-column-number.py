class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        char_0_code = ord('A') - 1
        result = 0

        for letter in columnTitle:
            result *= 26
            result += ord(letter) - char_0_code

        return result
