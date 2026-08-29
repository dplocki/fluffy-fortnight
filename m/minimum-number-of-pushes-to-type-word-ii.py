class Solution:
    def minimumPushes(self, word: str) -> int:
        mapping = {
            letter: index // 8 + 1
            for index, (letter, _) in enumerate(Counter(word).most_common())
        }

        return sum(
            mapping[letter]
            for letter in word
        )
