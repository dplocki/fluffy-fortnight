class Solution:
    def minWindow(self, s: str, t: str) -> str:
        string_length = len(s)
        string_letters = self.word_to_hash(s)
        substring_letters =  self.word_to_hash(t)

        results = []
        left, right = 0, 0

        window_letters = {}
        while True:
            while right < string_length:
                window_letters[s[right]] = window_letters.get(s[right], 0) + 1
                if self.check(window_letters, substring_letters):
                    break
                else:
                    right += 1

            if right == string_length:
                break
            else:
                results.append((left, right))

            while left < right:
                window_letters[s[left]] = window_letters[s[left]] - 1
                if not self.check(window_letters, substring_letters):
                    break
                else:
                    left += 1

            if left < right:
                results.append((left, right))

        if not results:
            return ''

        minum = min(results, key=lambda t: t[1] - t[0])
        return s[minum[0]:minum[1]]

    def check(self, s, t) -> str:
        return all(s.get(char, 0) >= t[char] for char in t)

    def word_to_hash(self, s: str):
        result = {}
        for c in s:
            result[c] = result.get(c, 0) + 1
        
        return result
