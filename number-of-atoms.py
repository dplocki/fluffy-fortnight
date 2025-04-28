class Solution:
    def countOfAtoms(self, formula: str) -> str:
        tokens = re.findall(r'[A-Z][a-z]?|\d+|[()]', formula)
        stack = [Counter()]

        multiplayer = 1
        for index, token in enumerate(tokens):
            if token == '(':
                stack.append(Counter())
            elif token == ')':
                pass
            
            if token.isdigit():
                multiplayer = int(token)
            else:
                multiplayer = 1

            if tokens[index - 1] == ')':
                bracket_result = stack.pop()
                for atom in bracket_result:
                    stack[-1][atom] = stack[-1][atom] + bracket_result.get(atom, 0) * multiplayer
            else:
                last_symbol = tokens[index - 1]
                stack[-1][last_symbol] = stack[-1][last_symbol] + (multiplayer - 1)

            if not token.isdigit():
                stack[-1][token] = stack[-1].get(token, 0) + 1

        return ''.join(key + (str(stack[0][key]) if stack[0][key] > 1 else '') for key in sorted(stack[0]))
