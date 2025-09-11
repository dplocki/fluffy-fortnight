class Solution:
    VOWELS = set('aAeEiIoOuU')

    def sortVowels(self, s: str) -> str:
        vowels = []

        for letter in s:
            if letter in Solution.VOWELS:
                vowels.append(letter)

        vowels = iter(sorted(vowels))
        return ''.join(
            next(vowels) if letter in Solution.VOWELS else letter
            for letter in s)
