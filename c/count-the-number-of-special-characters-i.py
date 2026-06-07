class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        letters = set(word)

        return sum(1
            for letter in letters
            if letter.islower() and letter.upper() in letters)
