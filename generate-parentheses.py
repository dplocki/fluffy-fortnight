class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        return list(self.internal(n, 0, 0, ''))

    def internal(self, n: int,  open_bracket_count: int, close_bracket_count: int, combination: str):
        if open_bracket_count > n or close_bracket_count > n or close_bracket_count > open_bracket_count:
            return

        if open_bracket_count == n == close_bracket_count:
            yield combination
        else:
            yield from self.internal(n, open_bracket_count + 1, close_bracket_count, combination + '(')
            yield from self.internal(n, open_bracket_count, close_bracket_count + 1, combination + ')')
