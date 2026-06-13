class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        return ''.join(
            chr(ord('a') + 25 - (self.word_weight(weights, word) % 26))
            for word in words
        )

    def word_weight(self, weights: List[int], word: str) -> int:
        return sum(weights[ord(letter) - ord('a')] for letter in word)
