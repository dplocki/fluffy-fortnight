class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        return list(self.internal(n, n, ''))

    def internal(self, open_bracket_count: int, close_bracket_count: int, combination: str):
        if open_bracket_count < 0 or close_bracket_count < 0 or close_bracket_count < open_bracket_count:
            return

        if open_bracket_count == close_bracket_count == 0:
            yield combination
        else:
            yield from self.internal(open_bracket_count - 1, close_bracket_count, combination + '(')
            yield from self.internal(open_bracket_count, close_bracket_count - 1, combination + ')')
