class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        result, current = 0, 0

        for letter in s:
            if letter == ')':
                if current <= 0:
                    result += 1
                else:
                    current -= 1
            else:
                current += 1

        return result + current 
