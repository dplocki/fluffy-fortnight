class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = [[]]

        for letter in s:
            if letter == ')':
                tmp = stack.pop()
                stack[-1].extend(tmp[::-1])
            elif letter == '(':
                stack.append([])
            else:
                stack[-1].append(letter)

        return ''.join(stack[0])
