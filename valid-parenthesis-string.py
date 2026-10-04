class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)
        
        @cache
        def internal(index: int, open_brackets: int) -> bool:
            if open_brackets < 0:
                return False

            if index == n:
                return open_brackets == 0

            if s[index] == '(':
                return internal(index + 1, open_brackets + 1)
            elif s[index] == ')':
                return internal(index + 1, open_brackets - 1)

            return (
                internal(index + 1, open_brackets - 1) or 
                internal(index + 1, open_brackets) or 
                internal(index + 1, open_brackets + 1)
            )

        return internal(0, 0)
