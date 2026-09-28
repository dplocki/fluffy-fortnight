class Solution:
    def maxDepth(self, s: str) -> int:
        result, current_deep = 0, 0

        for letter in s:
            if letter == '(':
                current_deep += 1
                result = max(result, current_deep)
            elif letter == ')':
                current_deep -= 1

        return result
