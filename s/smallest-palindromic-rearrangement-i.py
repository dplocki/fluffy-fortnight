class Solution:
    def smallestPalindrome(self, s: str) -> str:
        letters = Counter(s)
        result = ''
        center = None

        for letter in ascii_lowercase:
            if letter not in letters:
                continue

            number = letters[letter]
            if number % 2 == 1:
                center = letter
                number -= 1

            result += letter * (number >> 1)

        return result + (center if center else '') + result[::-1]
