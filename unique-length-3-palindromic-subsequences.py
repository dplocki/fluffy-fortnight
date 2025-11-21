class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        checked = set()
        result = 0

        for start, letter in enumerate(s):
            if letter in checked:
                continue

            end = s.rfind(letter)
            if end <= start:
                continue

            result += len(set(s[start + 1:end]))
            checked.add(letter)
        
        return result
