class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        level, result = 0, []

        for character in s:
            if character == '(':
                level += 1

            if level > 1:
                result.append(character)

            if character == ')':
                level -= 1

        return ''.join(result)
