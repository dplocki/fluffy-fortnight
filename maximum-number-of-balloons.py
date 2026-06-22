NEEDED_LETTERS = Counter('balloon')

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counter = Counter(text)

        return min(
            counter[letter] // count
            for letter, count in NEEDED_LETTERS.items()
        )
