class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        n = len(expression)
        self.current = 0

        def parse():
            groups = [[]]

            while self.current < n and expression[self.current] != '}':
                token = expression[self.current]
                self.current += 1

                if token == '{':
                    groups[-1].append(parse())
                elif token == ',':
                    groups.append([])
                else:
                    groups[-1].append({token})

            if self.current < n and expression[self.current] == '}':
                self.current += 1

            result = set()
            for group in groups:
                combined = {''}
                for s in group:
                    combined = {a + b for a in combined for b in s}
                result |= combined

            return result


        return sorted(parse())
