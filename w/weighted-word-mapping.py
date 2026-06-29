LETTERS_START = ord('a')

class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        return ''.join(
            chr(
                LETTERS_START + 25 - (sum(weights[ord(letter) - LETTERS_START] for letter in word) % 26)
            )
            for word in words
        )
