class Solution:
    def processStr(self, s: str) -> str:
        result = []

        for character in s:
            if character == '*':
                if result: result.pop()
            elif character == '#':
                result = result * 2
            elif character == '%':
                result = result[::-1]
            else:
                result.append(character)

        return ''.join(result)
