class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        broken_letters = set(brokenLetters)
        
        return sum(
            0 if word & broken_letters else 1
            for word in map(set, text.split()))
