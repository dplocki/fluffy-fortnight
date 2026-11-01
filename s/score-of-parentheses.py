class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []

        for letter in s:
            if letter == '(':
                stack.append(letter)
            elif letter == ')':
                result = 0
                while stack:
                    top_value = stack.pop()
                    if top_value == '(':
                        result <<= 1
                        break
 
                    result += top_value

                if result == 0:
                    result = 1
 
                stack.append(result)

        return sum(stack)
