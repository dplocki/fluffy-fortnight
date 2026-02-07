class Solution:
    OPERATIONS = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,
    }

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token in Solution.OPERATIONS:
                b, a = stack.pop(), stack.pop()
                stack.append(int(Solution.OPERATIONS[token](a, b)))
            else:
                stack.append(int(token))

        return stack[0]
