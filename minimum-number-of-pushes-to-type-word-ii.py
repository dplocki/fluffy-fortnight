class Solution:
    def minimumPushes(self, word: str) -> int:
        mapping = {}
        for index, (letter, count) in enumerate(Counter(word).most_common()):
            mapping[letter] = index // 8 + 1
        
        return sum(
            mapping[letter]
            for letter in word
        )
