class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []

        for letter in s:
            if letter == ')':
                tmp = []
                while stack[-1] != '(':
                    tmp.append(stack.pop())

                stack.pop()
                stack += tmp
                continue

            stack.append(letter)

        return ''.join(stack)
