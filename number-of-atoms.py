class Solution:
    def countOfAtoms(self, formula: str) -> str:
        tokens = re.findall(r'[A-Z][a-z]*|\d+|[()]', formula)
        tokens.append('$')
        stack = [Counter()]
        
        multiplayer = 1
        for index, token in enumerate(tokens):
            if token.isdigit():
                multiplayer = int(token)
            else:
                multiplayer = 1

            if not tokens[index - 1].isdigit():
                if tokens[index - 1] == ')':
                    bracket_result = stack.pop()
                    for atom in bracket_result:
                        stack[-1][atom] = stack[-1][atom] + bracket_result.get(atom, 0) * multiplayer
                elif tokens[index - 1] == '(' or tokens[index - 1] == '$':
                    pass
                else:
                    last_symbol = tokens[index - 1]
                    stack[-1][last_symbol] = stack[-1][last_symbol] + multiplayer

            if token == '$':
                break

            if token == '(':
                stack.append(Counter())

        return ''.join(key + (str(stack[0][key]) if stack[0][key] > 1 else '') for key in sorted(stack[0]))
