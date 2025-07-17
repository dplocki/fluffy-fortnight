class Solution:
    def isValid(self, word: str) -> bool:
        word_len = len(word)
        if word_len < 3:
            return False

        word = word.lower()
        for v in 'aeiou':
            word = word.replace(v, '')

        new_len = len(word)
        if new_len == word_len:
            return False

        word_len = new_len
        for l in ascii_lowercase:
            word = word.replace(l, '')

        new_len = len(word)
        if new_len == word_len:
            return False

        word_len = new_len
        for d in '0123456789':
            word = word.replace(d, '')

        return len(word) == 0
