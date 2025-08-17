class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)

        @cache
        def internal(subword: str) -> bool:
            if subword in words:
                return True

            for split_index in range(1, len(subword)):
                if internal(subword[:split_index]) and internal(subword[split_index:]):
                    return True

            return False

        return internal(s)
