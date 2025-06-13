class Solution:
    def isPalindrome(self, s: str) -> bool:
        internal = [character for character in s.lower() if character.isalnum()]
        characters_count = len(internal)

        return all(
            internal[i] == internal[characters_count - i - 1]
            for i in range(characters_count >> 1))
