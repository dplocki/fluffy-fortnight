class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        max_s = len(s)
        words = set(wordDict)
        word_lengths = set(map(len, words))
        current = []

        def internal(start: int):
            if start == max_s:
                yield ' '.join(current)
                return

            for word_length in word_lengths:
                sub_string = s[start:start + word_length]
                if sub_string not in words:
                    continue

                current.append(sub_string)
                yield from internal(start + word_length)
                current.pop()

        return list(internal(0))
