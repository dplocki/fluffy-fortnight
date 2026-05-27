class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lowers, uppers = {}, {}
        for index, letter in enumerate(word ):
            if letter.islower():
                lowers[letter] = index
            elif letter not in uppers:
                uppers[letter] = index

        return sum(1
            for letter, last in lowers.items()
            if uppers.get(letter.upper(), 0) > last)
