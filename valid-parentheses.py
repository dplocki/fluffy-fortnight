class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for character in s:
            if character == '(' or character == '[' or character == '{':
                stack.append(character)
            elif character == ')' or character == ']' or character == '}':
                bracket = stack.pop() if stack else None
                if (bracket == '(' and character == ')') or \
                    (bracket == '[' and character == ']') or \
                    (bracket == '{' and character == '}'):
                    continue

                return False

        return not stack
